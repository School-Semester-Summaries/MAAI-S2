# Code Genereren
Ik heb GenAI gebruikt om al mijn code te generen. Hier voorbeelden van files die gegenereerde code bevatten:
- [Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/)
- [XGBoost_v9.1](../../../code/)
- [DQN_v7.2](../../../code/)
- [Comparison Notebook_v0.1.ipynb](../../../code/)
- [app.py](../../../code/)

Hier zijn twee voorbeelden van hoe ik gegenereerde code verander:

## Example 1

Prompt
```md
# Print Fan_Out transactions — suspicious and normal, caught and missed
n=10

fan_out_analysis = val_analysis_eng[val_analysis_eng['Laundering_type'] == 'Fan_Out']
normal_fan_out_analysis = val_analysis_eng[val_analysis_eng['Laundering_type'] == 'Normal_Fan_Out']

print(f'\n{"="*60}')
print('Fan_Out (SUSPICIOUS) — predicted SUSPICIOUS (correctly caught)')
print(f'{"="*60}')
print(fan_out_analysis[fan_out_analysis['predicted_label'] == 1].head(n).to_string(index=False))

print(f'\n{"="*60}')
print('Fan_Out (SUSPICIOUS) — predicted NORMAL (missed)')
print(f'{"="*60}')
print(fan_out_analysis[fan_out_analysis['predicted_label'] == 0].head(n).to_string(index=False))

print(f'\n{"="*60}')
print('Normal_Fan_Out (NORMAL) — predicted NORMAL (correctly ignored)')
print(f'{"="*60}')
print(normal_fan_out_analysis[normal_fan_out_analysis['predicted_label'] == 0].head(n).to_string(index=False))

print(f'\n{"="*60}')
print('Normal_Fan_Out (NORMAL) — predicted SUSPICIOUS (false positive)')
print(f'{"="*60}')
print(normal_fan_out_analysis[normal_fan_out_analysis['predicted_label'] == 1].head(n ).to_string(index=False))

rewrite this for fan in
```

Answer
```python
# Print Fan_In transactions — suspicious and normal, caught and missed
n = 10

fan_in_analysis        = val_analysis_eng[val_analysis_eng['Laundering_type'] == 'Fan_In']
normal_fan_in_analysis = val_analysis_eng[val_analysis_eng['Laundering_type'] == 'Normal_Fan_In']

print(f'\n{"="*60}')
print('Fan_In (SUSPICIOUS) — predicted SUSPICIOUS (correctly caught)')
print(f'{"="*60}')
print(fan_in_analysis[fan_in_analysis['predicted_label'] == 1].head(n).to_string(index=False))

print(f'\n{"="*60}')
print('Fan_In (SUSPICIOUS) — predicted NORMAL (missed)')
print(f'{"="*60}')
print(fan_in_analysis[fan_in_analysis['predicted_label'] == 0].head(n).to_string(index=False))

print(f'\n{"="*60}')
print('Normal_Fan_In (NORMAL) — predicted NORMAL (correctly ignored)')
print(f'{"="*60}')
print(normal_fan_in_analysis[normal_fan_in_analysis['predicted_label'] == 0].head(n).to_string(index=False))

print(f'\n{"="*60}')
print('Normal_Fan_In (NORMAL) — predicted SUSPICIOUS (false positive)')
print(f'{"="*60}')
print(normal_fan_in_analysis[normal_fan_in_analysis['predicted_label'] == 1].head(n).to_string(index=False))
```

## Example 2
Het prototype is gegenereerd door Claude. Dit was een ontzettend lang proces en niet alle prompts gaan besproken worden omdat dat echt heel lang gaat duren en geen meerwaarde levert.

Prompt
```md
i want a tab with recent transactions, i also want somewhere a tab where you can set the threshold which also shows the recall and precision and amount of laundering cases fp per tp etc. after setting this threshold, you will get x amount of transactions up for review, that you can manually review. there should also be a top 3 features that show why this got flagged, shap explanations should be turned into percentages rather than shap points for better readability. there should also be an option to see the full shap percentage report so you can see all features. feature names should be understandable for a user. tool most be easy to use and understandable for someone that isnt IT or Data scientist
```

Answer
```md
Great spec. Let me build this. First let me check the skills available.

Check available skills for frontend development

Check available skills for frontend developmentGood. Now let me build this. This is a substantial app — I'll build it as a React artifact with mock data since we can't load your actual model files in the browser, but structured exactly as you described.

Action: Starts building react app
```

Prompt
```md
cant we just make a simple streamlit? i think react is overkill for a minimal prototype?
```

Answer
```
Yes, Streamlit is much more appropriate for a prototype like this. It is faster to build, easier to run locally, and more realistic as a deployable tool.
The only catch is I cannot run it here since it requires your model files and data locally. But I can write the full Python script that you run on your own machine.
You will need:

The XGBoost model JSON file
The DQN .pt file
The test CSV
Your trained StandardScaler

What are the file paths for those on your machine?
```

> veel gerodzooi met file locations, files leveren aan claude bla bla bla. dus we skippen even een paar prompts

Answer
```md
For file locations, create this folder structure:

aml_prototype/
├── app.py              ← the streamlit app
├── models/
│   ├── xgb_it3.json    ← your XGBoost model
│   ├── dqn_it2.pt      ← your DQN model
│   └── scaler.pkl      ← save this from notebook
└── data/
    └── test.csv        ← your test set from dataset_FE_2/test.csv

Also save your one-hot encoded column names since the app needs to know the feature order:

pythonimport json
with open('aml_prototype/models/feature_names.json', 'w') as f:
    json.dump(X_train_enc.columns.tolist(), f)

Once you have those files in place I can write the full app.py. Shall I proceed?
```

Prompt
```md
yes write it
```

Answer
```
Here is the app. To run it:

Create the folder structure I described earlier
Save scaler and feature names from your notebook
Install dependencies: pip install streamlit xgboost shap joblib torch scikit-learn
Run: streamlit run app.py from inside the aml_prototype/ folder

What it does:

Sidebar model selector (XGBoost IT3 / DQN IT2) and threshold slider
Live metrics: transactions flagged, recall, precision, false alerts per genuine case
Tab 1: table of all flagged transactions, click to select one
Tab 2: full transaction detail with suspiciousness score, top 3 SHAP reasons in plain English, and an expandable full explanation

Let me know when you have it running and we can refine anything.

Appendix: [app.py](./app.py)
```

Hierna is nog uren lang door gepropmt. Niet echt iets interessant gebeurd dat ik kan opbrengen
