# Dataset
For my dataset I have considered multiple widely known AML datasets, such as the IBM dataset [[1]](#1-ibm-transactions-for-anti-money-laundering-aml---httpswwwkagglecomdatasetsealtman2019ibm-transactions-for-anti-money-laundering-aml), SynthAML[[2]](#2-synthaml-dataset---httpsspringernaturefigsharecomcollectionssynthaml_a_synthetic_data_set_to_benchmark_anti-money_laundering_methods65044211) and SAML-D [[3]](#3-saml-d-dataset---httpswwwkagglecomdatasetsberkanoztassynthetic-transaction-monitoring-dataset-aml). However the issue with each dataset is that they aren't labelled. For RL, I need to create rewards for the model to understand when it is performing well and when it isn't. If there are no labels, both me and the model wouldn't know when the model is performing well or not.

There is one dataset that I found which has an is_fraud column. However, this dataset only has 2430 rows [[4]](#4-money-laundering-data---httpswwwkagglecomdatasetsmaryam1212money-laundering-datadata). Instead of proceeding with a small dataset. I decided to create my own using tools like: AMLSim [[5]](#5-amlsim---httpsknowledgeiadborgenknowledge-resourcescode-developmentopen-source-solutionamlsimutm_sourcechatgptcom) or AMLGentex [[6]](#6-amlgentex---httpsgithubcomaidotseamlgentexutm_sourcechatgptcom). These tools are designed to created syntehtic datasets for AML.


## Bibliography
#### 1. IBM Transactions for Anti Money Laundering (AML) - https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml
#### 2. SynthAML Dataset - https://springernature.figshare.com/collections/SynthAML_a_Synthetic_Data_Set_to_Benchmark_Anti-Money_Laundering_Methods/6504421/1
#### 3. SAML-D Dataset - https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml
#### 4. Money Laundering Data - https://www.kaggle.com/datasets/maryam1212/money-laundering-data/data
#### 5. AMLSim - https://knowledge.iadb.org/en/knowledge-resources/code-development/open-source-solution/amlsim?utm_source=chatgpt.com
#### 6. AMLGentex - https://github.com/aidotse/AMLGentex?utm_source=chatgpt.com