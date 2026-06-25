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
    if model_choice == 'XGBoost IT3':
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

def friendly(name):
    for k, v in FRIENDLY_NAMES.items():
        if name.startswith(k):
            return v
    return name.replace('_', ' ').capitalize()

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

def mask_account(account_id):
    s = str(int(account_id))
    return '*' * 5 + s[5:]

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
                <p style='color:#ccc;font-size:14px;margin-bottom:1rem;'>This is a research prototype. All transaction data is based on realistic synthetic patterns and does not contain real banking records. Human review is always required before acting on any alert.</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("I understand, continue", use_container_width=True):
                st.session_state['disclaimer_shown'] = True
                st.rerun()
        st.stop()

    st.title("🔍 AML Transaction Monitor")
    st.caption("Anti-Money Laundering review tool — for investigator use only")

    try:
        xgb_model, dqn, scaler, feature_names = load_resources()
        test_df = load_test_data()
    except Exception as e:
        st.error(f"Could not load model or data: {e}")
        st.stop()

    y_true = test_df['Is_laundering'].values if 'Is_laundering' in test_df.columns else None
    total_tx = len(test_df)

    with st.sidebar:
        st.header("Settings")
        model_choice = st.selectbox(
            "Model", ["XGBoost IT3", "DQN IT2"],
            help="XGBoost IT3 is the recommended model (AUPRC 0.9275). DQN IT2 is shown for comparison (AUPRC 0.6608)."
        )
        if model_choice == "DQN IT2":
            st.warning("⚠️ **Experimental model.** The DQN produces unreliable confidence scores and is not suitable for operational use. Results should be interpreted with caution and are shown for comparison purposes only.")

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
            slider_val = st.slider("Threshold", min_value=0.0, max_value=1.0,
                                   value=st.session_state['threshold'], step=0.001, format="%.3f")
        with col_s2:
            typed_val = st.number_input("", min_value=0.0, max_value=1.0,
                                        value=st.session_state['threshold'], step=0.001, format="%.3f",
                                        label_visibility='collapsed')

        if abs(typed_val - st.session_state['threshold']) > 0.0001:
            st.session_state['threshold'] = typed_val
        elif abs(slider_val - st.session_state['threshold']) > 0.0001:
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

    if y_true is not None and thresh_arr is not None:
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

    st.divider()

    tab1, tab2 = st.tabs([f"📋 Transactions for review ({n_flagged:,})", "🔎 Transaction detail"])

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
            flagged_sorted['Sender_account'] = flagged_sorted['Sender_account'].apply(mask_account)
            flagged_sorted['Receiver_account'] = flagged_sorted['Receiver_account'].apply(mask_account)
            flagged_sorted['Amount'] = flagged_sorted['Amount'].apply(lambda x: f'£{float(x):,.2f}')

            selected = st.dataframe(
                flagged_sorted[display_cols].reset_index(drop=True),
                use_container_width=True,
                selection_mode='single-row',
                on_select='rerun',
                key='flagged_table'
            )

            if selected and selected.selection.rows:
                row_idx = selected.selection.rows[0]
                actual_idx = flagged_sorted.index[row_idx]
                st.session_state['selected_idx'] = actual_idx
                st.info("Transaction selected — switch to the **Transaction detail** tab to review.")

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
                'Sender account':    mask_account(row['Sender_account']),
                'Receiver account':  mask_account(row['Receiver_account']),
                'Amount':            f'£{float(row["Amount"]):,.2f}',
                'Payment type':      row['Payment_type'],
                'Payment currency':  row['Payment_currency'],
                'Received currency': row['Received_currency'],
                'Sender location':   row['Sender_bank_location'],
                'Receiver location': row['Receiver_bank_location'],
                'Confidence':        f'{score_val * 100:.1f}%',
                'Status':            '🚨 FLAGGED' if is_flagged else '✅ NOT FLAGGED',
            }
            if show_actual and actual is not None:
                summary_row['Actual label'] = '🚨 Laundering' if actual == 1 else '✅ Normal'
            if show_actual and 'Laundering_type' in row.index:
                summary_row['Laundering type'] = row['Laundering_type']

            st.dataframe(pd.DataFrame([summary_row]), use_container_width=True, hide_index=True)

            st.divider()

            st.subheader("Why was this transaction flagged?")
            st.caption("Each feature's percentage contribution to the confidence score.")

            with st.spinner("Computing explanation..."):
                row_xgb = X_xgb_full.loc[[idx]] if idx in X_xgb_full.index else X_xgb_full.iloc[[list(test_df.index).index(idx)]]
                shap_pct = get_shap_percentages(row_xgb, xgb_model)

            if shap_pct:
                top3 = list(shap_pct.items())[:3]
                st.write("**Top 3 reasons:**")
                for feat, pct in top3:
                    colour = "🔴" if pct > 0 else "🟢"
                    feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                    direction = "increases" if pct > 0 else "decreases"
                    st.write(f"{colour} **{friendly(feat)}** (value: {feat_val}) — {direction} suspicion by {abs(pct):.1f}%")

                with st.expander("View full explanation"):
                    suspicious_feats = sorted([(f, p) for f, p in shap_pct.items() if p > 0.1], key=lambda x: x[1], reverse=True)
                    normal_feats = sorted([(f, p) for f, p in shap_pct.items() if p < -0.1], key=lambda x: x[1])

                    col_red, col_green = st.columns(2)
                    with col_red:
                        st.markdown("**🔴 Increases suspicion**")
                        for feat, pct in suspicious_feats:
                            feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                            st.markdown(f"<span style='color:{shade_red(pct)}'>{friendly(feat)} ({feat_val}): +{pct:.1f}%</span>", unsafe_allow_html=True)
                    with col_green:
                        st.markdown("**🟢 Decreases suspicion**")
                        for feat, pct in normal_feats:
                            feat_val = row_xgb.iloc[0][feat] if feat in row_xgb.columns else '—'
                            st.markdown(f"<span style='color:{shade_green(pct)}'>{friendly(feat)} ({feat_val}): {pct:.1f}%</span>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
