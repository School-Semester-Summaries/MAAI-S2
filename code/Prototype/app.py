import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import torch
import torch.nn as nn
import torch.nn.functional as F
import shap
import joblib
import json
import matplotlib
matplotlib.use('Agg')
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="AML Transaction Monitor", page_icon="🔍", layout="wide")

FRIENDLY_NAMES = {
    'pair_tx_count':              'Times this sender-receiver pair has transacted before',
    'Payment_type':               'Payment method',
    'sender_amount_std':          'Variation in sender transaction amounts',
    'receiver_tx_count':          'Number of transactions received by this account',
    'receiver_amount_std':        'Variation in receiver transaction amounts',
    'sender_unique_receivers':    'Number of unique accounts this sender has paid',
    'receiver_amount_mean':       'Average amount received by this account',
    'sender_amount_max':          'Largest amount ever sent by this sender',
    'sender_amount_min':          'Smallest amount ever sent by this sender',
    'fan_out_ratio':              'Ratio of unique receivers to total sends',
    'receiver_unique_senders':    'Number of unique accounts that have paid this receiver',
    'sender_amount_mean':         'Average amount sent by this sender',
    'fan_in_ratio':               'Ratio of unique senders to total receives',
    'sender_tx_count':            'Total transactions sent by this sender',
    'sender_unique_currencies':   'Number of different currencies used by sender',
    'sender_unique_locations':    'Number of different locations sender has sent from',
    'receiver_unique_currencies': 'Number of different currencies received',
    'receiver_unique_locations':  'Number of different locations receiver is in',
    'is_cross_currency':          'Payment and received currency differ',
    'is_cross_border':            'Sender and receiver are in different countries',
    'Amount':                     'Transaction amount',
}

RATIO_FEATURES = {'fan_out_ratio', 'fan_in_ratio'}

class QNetwork(nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_features, 124), nn.ReLU(),
            nn.Linear(124, 62),         nn.ReLU(),
            nn.Linear(62,  31),         nn.Tanh(),
            nn.Linear(31,  15),
            nn.Linear(15,   2),
        )
    def forward(self, x):
        return self.net(x)

@st.cache_resource
def load_resources():
    xgb_model = xgb.XGBClassifier()
    xgb_model.load_model('models/xgboost_aml_optuna.json')
    with open('models/feature_names.json') as f:
        feature_names = json.load(f)
    scaler = joblib.load('models/scaler.pkl')
    dqn = QNetwork(n_features=len(feature_names))
    dqn.load_state_dict(torch.load('models/dqn_v2_best.pt', map_location='cpu'))
    dqn.eval()
    return xgb_model, dqn, scaler, feature_names

@st.cache_data
def load_test_data():
    return pd.read_csv('data/test.csv', nrows=20893)

def prepare_xgb_features(df):
    DROP = ['Is_laundering', 'Laundering_type']
    CAT_COLS = ['Payment_currency', 'Received_currency',
                'Sender_bank_location', 'Receiver_bank_location', 'Payment_type']
    X = df.drop(columns=[c for c in DROP if c in df.columns]).copy()
    for col in CAT_COLS:
        if col in X.columns:
            X[col] = X[col].astype('category')
    return X

def prepare_dqn_features(df, scaler, feature_names):
    DROP = ['Is_laundering', 'Laundering_type']
    CAT_COLS = ['Payment_currency', 'Received_currency',
                'Sender_bank_location', 'Receiver_bank_location', 'Payment_type']
    X = df.drop(columns=[c for c in DROP if c in df.columns]).copy()
    X = pd.get_dummies(X, columns=[c for c in CAT_COLS if c in X.columns])
    X = X.reindex(columns=feature_names, fill_value=0)
    return scaler.transform(X).astype(np.float32)

def score_batch(df, xgb_model, dqn, scaler, feature_names, model_choice):
    X_xgb = prepare_xgb_features(df)
    if model_choice == 'XGBoost-I3':
        scores = xgb_model.predict_proba(X_xgb)[:, 1]
    else:
        X_sc = prepare_dqn_features(df, scaler, feature_names)
        with torch.no_grad():
            t = torch.FloatTensor(X_sc)
            q = dqn(t)
            scores = F.softmax(q, dim=1)[:, 1].numpy()
    return scores, X_xgb

def get_shap_percentages(row_xgb, xgb_model):
    explainer = shap.TreeExplainer(xgb_model)
    row_coded = row_xgb.copy()
    for col in row_coded.select_dtypes('category').columns:
        row_coded[col] = row_coded[col].cat.codes
    sv = explainer(row_coded)
    vals = sv.values[0]
    total = np.sum(np.abs(vals))
    if total == 0:
        return {}
    names = row_coded.columns.tolist()
    pct = {names[i]: round(float(vals[i]) / total * 100, 1) for i in range(len(names))}
    return dict(sorted(pct.items(), key=lambda x: abs(x[1]), reverse=True))

def get_shap_percentages_dqn(row_sc, dqn, background_sc, feature_names):
    def dqn_predict(X):
        dqn.eval()
        with torch.no_grad():
            t = torch.FloatTensor(X).to('cpu')
            q = dqn(t)
            probs = torch.softmax(q, dim=1)[:, 1]
        return probs.numpy()

    explainer = shap.KernelExplainer(dqn_predict, background_sc[:100])
    sv = explainer.shap_values(row_sc, nsamples=100)
    vals = np.array(sv).flatten()
    total = np.sum(np.abs(vals))
    if total == 0:
        return {}
    pct = {feature_names[i]: round(float(vals[i]) / total * 100, 1) for i in range(len(feature_names))}
    return dict(sorted(pct.items(), key=lambda x: abs(x[1]), reverse=True))

def friendly(name):
    for k, v in FRIENDLY_NAMES.items():
        if name.startswith(k):
            return v
    return name.replace('_', ' ').capitalize()

def format_feat_val(feat, val):
    """Format feature value for display. Ratio features shown as percentages,
    amount-based features rounded to 2 decimals."""
    if val == '—':
        return val
    if any(feat.startswith(r) for r in RATIO_FEATURES):
        try:
            return f'{float(val) * 100:.1f}%'
        except (ValueError, TypeError):
            return val
    if 'amount' in feat.lower():
        try:
            return f'{float(val):.2f}'
        except (ValueError, TypeError):
            return val
    return val

def shade_red(pct):
    return '#ff6b6b'

def shade_green(pct):
    return '#51cf66'

def threshold_for_recall(recall_target, recall_arr, thresh_arr):
    idx = np.argmin(np.abs(recall_arr[:-1] - recall_target))
    return float(thresh_arr[idx])

def threshold_for_precision(prec_target, precision_arr, thresh_arr):
    valid = np.where(precision_arr[:-1] >= prec_target)[0]
    if len(valid) == 0:
        return float(thresh_arr[-1])
    return float(thresh_arr[valid[0]])

def main():
    for key, default in [('disclaimer_shown', False), ('threshold', 0.074), ('show_actual', False)]:
        if key not in st.session_state:
            st.session_state[key] = default

    if not st.session_state['disclaimer_shown']:
        st.markdown("<style>.stApp { background-color: #0a0a0a; }</style>", unsafe_allow_html=True)
        _, col_mid, _ = st.columns([1, 2, 1])
        with col_mid:
            st.markdown("""
            <div style='background:#1e1e1e;padding:2rem;border-radius:12px;border:1px solid #444;margin-top:8rem;'>
                <h3 style='color:white;margin-bottom:0.5rem;'>⚠️ Prototype notice</h3>
                <p style='color:#ccc;font-size:14px;margin-bottom:1rem;'>This is a research prototype. <strong style='color:#fff;'>All transaction data is synthetic</strong> and does not contain real banking records. Human review is always required before acting on any alert.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("I understand, continue", use_container_width=True):
                st.session_state['disclaimer_shown'] = True
                st.rerun()
        st.stop()

    st.title("Transaction Monitor")
    st.caption("Anti-Money Laundering review tool")

    try:
        xgb_model, dqn, scaler, feature_names = load_resources()
        test_df = load_test_data()
    except Exception as e:
        st.error(f"Could not load model or data: {e}")
        st.stop()

    y_true = test_df['Is_laundering'].values if 'Is_laundering' in test_df.columns else None
    total_tx = len(test_df)

    col_model, _ = st.columns([1, 2])
    with col_model:
        model_choice = st.selectbox(
            "🤖 Model", ["XGBoost-I3", "DQN-I2"],
            help="XGBoost-I3 is the recommended model. DQN-I2 is shown for comparison."
        )
    if model_choice == "DQN-I2":
        st.warning("⚠️ **Experimental model.** The DQN produces unreliable confidence scores and is not suitable for operational use. Results should be interpreted with caution and are shown for comparison purposes only.")

    with st.sidebar:
        st.header("Settings")
        st.divider()
        st.subheader("Detection threshold")
        st.caption("Transactions with a confidence score above this threshold are flagged for review.")

        with st.spinner("Computing scores..."):
            scores, X_xgb_full = score_batch(test_df, xgb_model, dqn, scaler, feature_names, model_choice)

        if y_true is not None:
            precision_arr, recall_arr, thresh_arr = precision_recall_curve(y_true, scores)
        else:
            precision_arr = recall_arr = thresh_arr = None

        col_s1, col_s2 = st.columns([3, 1])
        with col_s1:
            slider_val_pct = st.slider("Threshold", min_value=0.0, max_value=100.0,
                                   value=st.session_state['threshold'] * 100, step=0.1, format="%.1f%%")
        with col_s2:
            typed_val_pct = st.number_input("", min_value=0.0, max_value=100.0,
                                        value=st.session_state['threshold'] * 100, step=0.1, format="%.1f",
                                        label_visibility='collapsed')

        slider_val = slider_val_pct / 100
        typed_val = typed_val_pct / 100

        if abs(typed_val - st.session_state['threshold']) > 0.000001:
            st.session_state['threshold'] = typed_val
        elif abs(slider_val - st.session_state['threshold']) > 0.000001:
            st.session_state['threshold'] = slider_val

        if thresh_arr is not None:
            st.caption("Or set threshold by target:")
            col_r, col_p = st.columns(2)
            with col_r:
                target_recall = st.number_input("Catch X% of cases", min_value=0.0, max_value=100.0, value=95.0, step=0.1)
                if st.button("Apply"):
                    st.session_state['threshold'] = threshold_for_recall(target_recall / 100, recall_arr, thresh_arr)
                    st.rerun()
            with col_p:
                target_prec = st.number_input("X% of alerts are real", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
                if st.button("Apply ", key='apply_prec'):
                    st.session_state['threshold'] = threshold_for_precision(target_prec / 100, precision_arr, thresh_arr)
                    st.rerun()

        st.divider()
        st.session_state['show_actual'] = st.toggle(
            "Show actual labels", value=st.session_state['show_actual'],
            help="Reveal whether flagged transactions are genuinely suspicious. Hidden by default to simulate real investigation conditions."
        )
        st.caption("Statistics are computed on the test set.")

    show_actual = st.session_state['show_actual']
    threshold = st.session_state['threshold']
    flagged_mask = scores >= threshold
    n_flagged = int(flagged_mask.sum())

    if y_true is not None and thresh_arr is not None and show_actual:
        idx_t = np.searchsorted(thresh_arr, threshold, side='right')
        idx_t = min(idx_t, len(precision_arr) - 1)
        prec_at_t = float(precision_arr[idx_t])
        rec_at_t  = float(recall_arr[idx_t])
        fp_per_tp = round((1 - prec_at_t) / prec_at_t) if prec_at_t > 0 else float('inf')

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Transactions flagged", f"{n_flagged:,} / {total_tx:,}")
        col2.metric("Cases caught", f"{rec_at_t:.1%}", help="Percentage of actual laundering transactions caught at this threshold")
        col3.metric("Alert accuracy", f"{prec_at_t:.1%}", help="Of every 100 flagged transactions, this many are genuine laundering cases")
        col4.metric("False alerts per genuine case", f"{fp_per_tp:,}" if fp_per_tp != float('inf') else "∞")
    else:
        st.metric("Transactions flagged", f"{n_flagged:,} / {total_tx:,}")

    st.divider()

    tab1, tab2, tab3 = st.tabs([f"📋 Transactions for review ({n_flagged:,})", "🔎 Transaction detail", "🔍 Account lookup"])

    with tab1:
        if n_flagged == 0:
            st.info("No transactions flagged at this threshold. Lower the threshold to flag more.")
        else:
            flagged_df = test_df[flagged_mask].copy()
            flagged_df['Confidence'] = [f'{s*100:.1f}%' for s in scores[flagged_mask]]

            display_cols = ['Sender_account', 'Receiver_account', 'Amount',
                            'Payment_type', 'Sender_bank_location', 'Receiver_bank_location', 'Confidence']

            if 'Is_laundering' in flagged_df.columns:
                flagged_df['Actual label'] = flagged_df['Is_laundering'].map({0: '✅ Normal', 1: '🚨 Laundering'})
                if show_actual:
                    display_cols.append('Actual label')

            if 'Laundering_type' in flagged_df.columns and show_actual:
                display_cols.append('Laundering_type')

            display_cols = [c for c in display_cols if c in flagged_df.columns]

            st.write(f"Showing {min(500, n_flagged):,} of {n_flagged:,} flagged transactions, sorted by confidence.")
            flagged_sorted = flagged_df.copy()
            flagged_sorted['_score'] = scores[flagged_mask]
            flagged_sorted = flagged_sorted.sort_values('_score', ascending=False).head(500)
            flagged_sorted['Amount'] = flagged_sorted['Amount'].apply(lambda x: f'£{float(x):,.2f}')

            selected = st.dataframe(
                flagged_sorted[display_cols].reset_index(drop=True),
                use_container_width=True,
                selection_mode='single-row',
                on_select='rerun',
                key=f'flagged_table_{model_choice}'
            )

            if selected and selected.selection.rows:
                row_idx = selected.selection.rows[0]
                actual_idx = flagged_sorted.index[row_idx]
                st.session_state['selected_idx'] = actual_idx
                st.session_state['selected_model'] = model_choice
                st.info("Transaction selected — switch to the **Transaction detail** tab to review.")

    if st.session_state.get('selected_model') != model_choice:
        st.session_state.pop('selected_idx', None)
        st.session_state.pop('selected_model', None)

    with tab2:
        if 'selected_idx' not in st.session_state:
            st.info("Select a transaction from the **Transactions for review** tab to inspect it here.")
        else:
            idx = st.session_state['selected_idx']
            row = test_df.loc[idx]
            score_val = float(scores[list(test_df.index).index(idx)])
            is_flagged = score_val >= threshold
            actual = int(row['Is_laundering']) if 'Is_laundering' in row else None

            summary_row = {
                'Sender account':    int(row['Sender_account']),
                'Receiver account':  int(row['Receiver_account']),
                'Amount':            f'£{float(row["Amount"]):,.2f}',
                'Payment type':      row['Payment_type'],
                'Payment currency':  row['Payment_currency'],
                'Received currency': row['Received_currency'],
                'Sender location':   row['Sender_bank_location'],
                'Receiver location': row['Receiver_bank_location'],
                'Confidence':        f'{score_val * 100:.1f}%',
            }
            if show_actual and actual is not None:
                summary_row['Actual label'] = '🚨 Laundering' if actual == 1 else '✅ Normal'
            if show_actual and 'Laundering_type' in row.index:
                summary_row['Laundering type'] = row['Laundering_type']

            st.dataframe(pd.DataFrame([summary_row]), use_container_width=True, hide_index=True)

            col_lookup1, col_lookup2 = st.columns(2)
            with col_lookup1:
                if st.button(f"🔍 Look up sender account ({int(row['Sender_account'])})", use_container_width=True):
                    st.session_state['lookup_account'] = int(row['Sender_account'])
                    st.session_state['active_tab'] = 'lookup'
            with col_lookup2:
                if st.button(f"🔍 Look up receiver account ({int(row['Receiver_account'])})", use_container_width=True):
                    st.session_state['lookup_account'] = int(row['Receiver_account'])
                    st.session_state['active_tab'] = 'lookup'

            if st.session_state.get('active_tab') == 'lookup':
                st.info("Account set for lookup — switch to the **Account lookup** tab to view results.")
                st.session_state.pop('active_tab', None)

            st.divider()

            st.subheader("Why was this transaction flagged?")
            st.caption("Each feature's percentage contribution to the confidence score.")

            row_xgb = X_xgb_full.loc[[idx]] if idx in X_xgb_full.index else X_xgb_full.iloc[[list(test_df.index).index(idx)]]

            if model_choice == "DQN-I2":
                with st.spinner("Computing explanation (this may take a moment)..."):
                    X_sc_full = prepare_dqn_features(test_df, scaler, feature_names)
                    row_sc = X_sc_full[[list(test_df.index).index(idx)]]
                    background_sc = X_sc_full[:100]
                    shap_pct = get_shap_percentages_dqn(row_sc, dqn, background_sc, feature_names)
            else:
                with st.spinner("Computing explanation..."):
                    shap_pct = get_shap_percentages(row_xgb, xgb_model)

            if shap_pct:
                top3 = list(shap_pct.items())[:3]
                st.write("**Top 3 reasons:**")
                for feat, pct in top3:
                    colour = "🔴" if pct > 0 else "🟢"
                    direction = "increases" if pct > 0 else "decreases"
                    if model_choice == "DQN-I2":
                        if '_' in feat and feat.split('_')[0] + '_' + feat.split('_')[1] in ['Payment_type', 'Payment_currency', 'Received_currency', 'Sender_bank', 'Receiver_bank']:
                            feat_val = feat.split('_', 2)[-1] if feat.count('_') >= 2 else feat
                        else:
                            feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                    else:
                        feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                    feat_val = format_feat_val(feat, feat_val)
                    st.write(f"{colour} **{friendly(feat)}** (value: {feat_val}) — {direction} suspicion by {abs(pct):.1f}%")

                with st.expander("View full explanation"):
                    suspicious_feats = sorted([(f, p) for f, p in shap_pct.items() if p > 0.1], key=lambda x: x[1], reverse=True)
                    normal_feats = sorted([(f, p) for f, p in shap_pct.items() if p < -0.1], key=lambda x: x[1])

                    col_red, col_green = st.columns(2)
                    with col_red:
                        st.markdown("**🔴 Increases suspicion**")
                        for feat, pct in suspicious_feats:
                            feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                            feat_val = format_feat_val(feat, feat_val)
                            st.markdown(f"<span style='color:{shade_red(pct)}'>{friendly(feat)} ({feat_val}): +{pct:.1f}%</span>", unsafe_allow_html=True)
                    with col_green:
                        st.markdown("**🟢 Decreases suspicion**")
                        for feat, pct in normal_feats:
                            feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                            feat_val = format_feat_val(feat, feat_val)
                            st.markdown(f"<span style='color:{shade_green(pct)}'>{friendly(feat)} ({feat_val}): {pct:.1f}%</span>", unsafe_allow_html=True)

            st.divider()
            st.subheader("File a report")

            if 'filed_reports' not in st.session_state:
                st.session_state['filed_reports'] = set()

            if idx in st.session_state['filed_reports']:
                st.success("✅ This transaction has already been reported and removed from the queue.")
            else:
                laundering_types = [
                    'Behavioural_Change_1', 'Behavioural_Change_2', 'Bipartite', 'Cash_Withdrawal',
                    'Cycle', 'Deposit-Send', 'Fan_In', 'Fan_Out', 'Gather-Scatter', 'Layered_Fan_In',
                    'Layered_Fan_Out', 'Normal_Cash_Deposits', 'Normal_Cash_Withdrawal', 'Normal_Fan_In',
                    'Normal_Fan_Out', 'Normal_Foward', 'Normal_Group', 'Normal_Mutual', 'Normal_Periodical',
                    'Normal_Plus_Mutual', 'Normal_Small_Fan_Out', 'Normal_single_large', 'Over-Invoicing',
                    'Scatter-Gather', 'Single_large', 'Smurfing', 'Stacked_Bipartite', 'Structuring'
                ]

                suspected = st.selectbox("What laundering pattern do you suspect?", laundering_types)

                if st.button("Submit report"):
                    actual_type = row['Laundering_type'] if 'Laundering_type' in row.index else 'Unknown'
                    actual_label = int(row['Is_laundering']) if 'Is_laundering' in row else None

                    if actual_label == 1:
                        if suspected == actual_type:
                            st.success(f"✅ Correct! This was indeed a laundering case of type **{actual_type}**.")
                        else:
                            st.warning(f"⚠️ This was a laundering case, but the pattern was **{actual_type}**, not {suspected}.")
                    else:
                        st.info(f"ℹ️ This was actually a **normal transaction** (type: {actual_type}). No laundering detected.")

                    st.session_state['filed_reports'].add(idx)
                    st.session_state.pop('selected_idx', None)

    with tab3:
        st.subheader("Account lookup")
        st.caption("Search for an account ID to view its full transaction history in the test set.")

        prefill = str(st.session_state.pop('lookup_account', '')) if 'lookup_account' in st.session_state else ''
        account_query = st.text_input("Account ID", value=prefill, placeholder="e.g. 6652024436")

        if account_query:
            try:
                account_id = int(account_query)
                mask = (test_df['Sender_account'] == account_id) | (test_df['Receiver_account'] == account_id)
                account_tx = test_df[mask].copy()

                if account_tx.empty:
                    st.info(f"No transactions found for account {account_id}.")
                else:
                    st.write(f"Found {len(account_tx):,} transaction(s) involving account {account_id}. Select a row to view it in **Transaction detail**.")

                    account_tx['Amount_display'] = account_tx['Amount'].apply(lambda x: f'£{float(x):,.2f}')
                    account_tx['Role'] = account_tx.apply(
                        lambda r: 'Sender' if r['Sender_account'] == account_id else 'Receiver', axis=1
                    )

                    display_cols = ['Sender_account', 'Receiver_account', 'Role', 'Amount_display',
                                    'Payment_type', 'Sender_bank_location', 'Receiver_bank_location']
                    if show_actual and 'Is_laundering' in account_tx.columns:
                        account_tx['Actual label'] = account_tx['Is_laundering'].map({0: '✅ Normal', 1: '🚨 Laundering'})
                        display_cols.append('Actual label')
                    if show_actual and 'Laundering_type' in account_tx.columns:
                        display_cols.append('Laundering_type')

                    display_cols = [c for c in display_cols if c in account_tx.columns]
                    rename_map = {'Amount_display': 'Amount'}

                    selected_lookup = st.dataframe(
                        account_tx[display_cols].rename(columns=rename_map).reset_index(drop=True),
                        use_container_width=True,
                        selection_mode='single-row',
                        on_select='rerun',
                        key='lookup_table'
                    )

                    if selected_lookup and selected_lookup.selection.rows:
                        row_idx = selected_lookup.selection.rows[0]
                        st.session_state['selected_idx'] = account_tx.index[row_idx]
                        st.session_state['selected_model'] = model_choice
                        st.info("Transaction selected — switch to the **Transaction detail** tab to review.")
            except ValueError:
                st.error("Please enter a valid numeric account ID.")


if __name__ == '__main__':
    main()
