# Dataset
For my dataset I have considered multiple widely known AML datasets, such as the IBM dataset, SynthAML and SAML-D. However the issue with each dataset is that they aren't labelled. For RL, I need to create rewards for the model to understand when it is performing well and when it isn't. If there are no labels, both me and the model wouldn't know when the model is performing well or not.

There is one dataset that I found which has an is_fraud column. However, this dataset only has 2430 rows [[.]](). Instead of proceeding with a small dataset. I decided to create my own using the AMLSim. AMLSim is a tool which allows you to create AML datasets.

## Bibliography
#### IBM Transactions for Anti Money Laundering (AML) - https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml
#### SynthAML Dataset - https://springernature.figshare.com/collections/SynthAML_a_Synthetic_Data_Set_to_Benchmark_Anti-Money_Laundering_Methods/6504421/1
#### SAML-D Dataset - https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml
#### Money Laundering Data - https://www.kaggle.com/datasets/maryam1212/money-laundering-data/data
