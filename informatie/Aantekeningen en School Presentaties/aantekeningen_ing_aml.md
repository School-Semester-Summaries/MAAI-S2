Michael Attard en Louis de Bruijn van ING 11 Maart 2023 Machine learning binne ING presentatie

Michael Attard
- Works at ING since 2024 October
- in transaction monitoring and customer due diligence

Louis de Bruijn
- at ING since 2020
- worked at customer dialogue, data anonymization.
- Works on transaction monitoring since 2022

Obligations for Banks
- Bank is manded by law to have systems in place that detect the presence of financial crime. in netherlands we have WWFT.
- If anything is detected they have to alarm the FIU
- We focus on 2 crimes
  - Money Laundering
  - Terrorist Financing: Using assets to faciliate terrorist activities
- Duties for banks
  - CDD/KYC > look longterm transaction history
  - Transaction Monitoring (TM) - Report unusual transactions > look short term transactions

General insights on Machine Learning
- why not rules engine?
  - we can build systems with set of rules to detect set of crimes. key problem is that it assumes that the programmer has a complete picture of what ruiles has to be put in place. 
  - if we go with a ML model we are independent of that. But the downside of ml models is that the set has to labeled since we use supervised.
- At ING we only do supervised classification models -> VRAAG -------------------------
  - Can be a linear boundary -> linear regression
  - can sometimes be more difficult boundaries -> Neural Networks

Imbalanced Data
- Our data is highly imbalanced
- Potential financial crime only reperesents 1 to 2% (We don't know how much is actually fraudelent) of the data we have the rest is legimiate
- different ways to fix imbalanced data -> see slides
- we cannot use accuracy since it would be very "accurate"
- We use precision and recall. 
  - Precision: how much percent is actually risky
  - Recall: of how much risky casees, how muhc did we catch
- AOPRC?
- labels are craeted as follows: rule goes of -> human checks and determines if this might be fraudelent or not.

Precision/Recall Demo
- You can optimize on recall but precision will suffer. And vice versa.
- *Demo starts
- What threshold is typically used?
- every company is first reviewed 3 times before being sent to the FUI
- during model dev we cant control the threshold by business. 
- using AUPRC to optimize the model -> So the reason to use AUPRC is to optimize precision and recall at the same time?
-> accruate feel on how well the model would perform on imbalanced data.
- we use this metric to give a feel on how well the model performs on imbalced data.
- we use this over AOC since that takes into account ... and that wouldn't give an accruate representation of the model performance since the data is imbalanced.
- we aim for recall 0.95. You can move the threshold as long as the recall is 0.95.

Generative AI in Banking
- We use GEN AI for:
  - KYC Summary Generation
  - Document Extraction
  - Hyper-Personlization - ING writes marketing messages. marketing specialist tries to make the marketing messages a bit more personal by dividing all people in for example 3 groups. For example: Young people, Mid, Old. 
  - Software Engineering
  - WB Front Office Productivity
  - WB AIDD GenAI Data Extraction
- Mortgages are INGs biggest incomes.

Customer Due Dilligence and Risk Assessment Model
- Not relevant for me.

TM
- ING has about 500 static rules to detect transaction as fraudelent
- tree based model perform well and are explainable, we use XGBoost, we generate low medium and high score.

Applied to Banking

Questions
1. In the context of transaction monitoring, You mentioned you use supervised classification for transaction monitoring and mentioned Logistic Regression and Neural Networks.
  1.1 Have you used anything else before using Logistic Regression and Neural Networks, trees like xgboost?
  1.2 Isn't NN problematic because of difficulty in explainability
  1.3 Are you limited by Bias and Explainability to choose different approaches, if so what direction woudld you like to go in if explainability and or bias wouldn't be a requirement.
2. In the context of TM, What are currently the biggest problems within AML within ING?
3. Has TMNL changed anything in your current workflow? (TMNL -> Share data with all banks)
4. What actions does ING take to comply to AVG?

Answers
1.1
1.2
1.3
2.
3.
4.


Other Questions
- 


Vraag de slides!!!
