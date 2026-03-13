ABN AMRO AML

Smrithi Menon
- DS 2 to 5 years
- From India

Tin Nguyen
- computer science & engineering / DS innovation team
- Vietnem

AML Methods
- human trafficking - payment and transfers regular intervals
- fraud/theft - sudden spike in bank balance
- internet scams
- drug trafficking - many small interactions
- tax evasion
- scam
- illegal wildlife
- ransoms
- bribery - lot of transfers between shel companies and lots of crypto transfers

Financial Crime: Global View
- 3 billion euros estimate of drug transport in nl
- 16 billion euros is laundred in netherlands
- netherlands is on 8th place of most laundered countries
- you cant write rules for every specific scenario. at one point it will explode. thats why we need machine learning
- money laundering originated at laundrettes, restaurants and ... because it is impossible to detect what money is from laundrette and what is from illegal origin
- transactions might not look suspicious on their own, but thats why we look at the patterns.

AML Cycle
Placement : riskiest layer
- structuring deposit into smaller amounts
- currency smuggling
- currency exchange
- blending funds
- false invoicing

Layering
- Multiple wire transfers
- purchase of asset
- converting cash into monetary instruments
- loan bank arrangements

Integration
- real...
- ...
- ...
- ...

> You can choose what step to build a model for. Layering is just not too difficult for models and just too difficult for rules to catch. so we focus on layering.

rule based vs machine learning in dfc
- before ml detection systems were prety much rule based.
  - if > threshold -> flag them
- rules were too static for dynamic changing world
- thats why we move to machine learning
- learn from historical patterns and let mmachines set the boundaries
- let the machine learn what is normal behaviour and hwat is suspicious
- we focus on improving true positives and reducing false positive

supervised vs unsupervised
- abn uses combination of supervised and unsupervised

Anomaly Behvaiour
- outlier doesnt mean specifically crime but worthy to investigate (is_suspicious)

Unsupervised models
- auto encoder
- clustering
- isolation forest

Flows, each transaction goes in both flows
Transactions -> Rules based model -> noise reduction ml model ---> investigator -> FUI
Transactions -> supervised models detect known forms of money laundering -> unsupervised models that detect unknown anomalous behaviour -> unsupervised models that detect anomalous behaviour ---> investigator -> FUI

SHAP values
- Everyone wants to know why was this customer alerted
- makes blackbox model more transparent
- provides a score for each feature
- contribute how features contribute positively or negatively
- we give a ranked list of these features along with the alert (top 3 features that alerted the alert along with the explanaiton of the features, shap values, and non technical explanation)
- what are usually top 3 most important faetures -> geography features like high risk, unusual cash tranasctions.
- giving top 3 features is enough of an explanation

KYC
- TM is about what the customer does KYC is who the customer is
- in KYC falls: past behaviours of customers, relationships, risk profiles
- client risk scoring (45% neutral, 30% medium, 10% increased, 15% unacceptable)
- more stuff about kyc that doesnt look relevant for my project

Questions
-1. can it make any model explainable?
0. can you explain what model you use to label data?
1. What models do you use within TM. (you mentioned combination of supervised and unsupervised)
3. Are you limited by Bias and Explainability to choose different approaches, if so what direction woudld you like to go in if explainability and or bias wouldn't be a requirement.
16. slides
17. evaluation metrics?
18. What decides what way takes a flow
19. when is precision mre important and when is recall more improtant?


Answers
-1. Maybe
0. Rules based model for labelling data. ---> but isnt using rules to label very erro prone -> yes it is! thats why we want to change it to ml models
1. xgboost, decision trees, random trees, autoencoder, clustering, isolation forest
3. computational power and costs. why nn if XGBoost same performance. why use more complex models if xgboost are also really good 
16. yes!
17. AUPR -> Precision Recall Curve -> good for imbalanced datasets
18. each transaction goese into both flows
19. Most cases focus on preciison, capture as many clients. but it is a difficult decision to make. All alerts are going to manual review so we have to discuess with them how many alerts are okay to review but we also want as much cases so we dicuss to find the best threshold. 

Kees
- vraag stakeholder
- hoe zit het met inleveren op dlo


Other
- What are shell companies?
- What falls under KYC?
