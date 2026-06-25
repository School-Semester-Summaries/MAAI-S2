Feedback Comments in "Master_Thesis_KG_v0.1_feedback_MB.docx" op  "Master_Thesis_KG_v0.1.pdf", including elaborations
status: afgerond

Terminology:
F = Feedback
-> = Mijn reactie/notitie op de feedback
F2 = Dezelfde feedback maar dan elaborated
T = Toepassing van de feedback
✅ = voldaan
🟨 = gedeeltelijk voldaan
❌ = niet voldaan

0. Abstract ✅
- updaten svp
-> ok
T: Abstract geschreven

1.1.3 Traditional AML Methods ✅
- Een afsluitende zin is hier nog op zijn plaats. Worden rule based systemen dan naast ML systemen gebruikt.
-> prima
T: stukje aangepast

Van
> *"While rule-based systems improved efficiency over manual review, they had limitations in handling complex laundering patterns and large-scale data, which led to the adoption of machine learning Menon and Nguyen (2026)."*

Naar
> *"While rule-based systems improved efficiency over manual review, their limitations in handling complex laundering patterns and large-scale data motivated machine learning as an additional layer to these systems Menon and Nguyen (2026)."*

1.2.2 RL an Emerging Method 🟨
- Ook hier mag wat meer toelichting, want je gaat RL uiteindelijk gebruiken. Dat mag hier maar ook einde van de paragraaf
-> ?
-> elaboration: concluderende zin in de richting van het is een promising methode etc.
T: herschreven, maar niet helemaal zoals gevraagd want dat vind ik dubbelop

Van
> *"To date, Reinforcement Learning has barely been explored within AML."*

Naar
> *"To date, Reinforcement Learning has barely been explored within AML. However, some research exists on the related topic of fraud detection, including:"*

1.4 Identified Gap ❌
- Hier nog verder uitwerken waarom die graph structures niet aanwezig zijn in de praktijk.
-> zoek dit uit
T: ik kon hier geen citeerbare bron voor vinden

2.1.2 Explainability with SHAP ✅
- begin de par. met deze zin. (Given the explainability requirements imposed by the Wwft, SHAP will be used in this research to interpret the decisions made by the RL model.)
-> prima
T: herschreven maar zonder requirement te benoemen want de requirements zijn in hoofdstuk 2 nog niet behandeld

Van
> *"SHAP (SHapley Additive exPlanations) is an explainability method that can be applied to any machine learning model, assigning each input feature a contribution score for a given prediction. This makes it particularly suitable for interpreting black-box models such as the Deep Q-Network used in this research..."*

Naar
> *"Explainability is a legal expectation in AML under the Wwft~\cite{wwft2008}, and this research therefore uses SHAP (SHapley Additive exPlanations) to interpret model decisions. SHAP is an explainability method that can be applied to any machine learning model, assigning each input feature a contribution score for a given prediction, making it particularly suitable for interpreting black-box models such as the Deep Q-Network used in this research..."*

2.3 AI Suitability Justification 🟨
- hier spreek je jezelf wat tegen: als xgboost zo goed is waarom dan nog RL gebruiken? geef aan waar toch de gap zit.
-> waarom nog RL gebruiken, omdat RL niet onderzocht is. het is niet zo explainable als xgboost wat ik ook aangeef maar er is een kans dat het xgboost zou outperformen en dan wordt het interessant, kies je voor xgboost, goede performance, goede explainability, of dqn met nog hogere performance, maar iets lagere explainability. in het geval dat dqn lager performt is het minder interessant, maar dit zoek ik dus uit.
-> elaboration: 1.5 lees identified gap, wrm zou je xgboost onderzoeken als RL al zo goed is check 1.5
T: niets veranderd. wrm xgboost onderzoeken? omdat er geen litertuur over bestaat en dus waarschijnlijk geen serieus onderzoek naar gedaan is.

3.4 Comparison Logic ✅
- voorwaarde voor dqn is dat het ook nog exlainable moet zijn, niet alleen beter.
-> goed punt
T: Comparison Logic wordt nu besproken in H4 results en benoemd alle criteria van Leeruitkomst C2

5.3 Preprocessing ✅
- where is table 8?
-> boven de comment
T: -

6.4.3 Training Mechanics ✅
- 2 iteraties lijkt me een prima begin maar wat zou een 3e (of 4e) iteratie opleveren? Doe je dat niet, dan graag beschrijven waarom dat geen verbetering oplevert.
-> goed punt, ik ga verder kijken
T: Verder geitereerd en gestopt met logische verantwoording

6.5 Observed Trade-offs ✅
- Zou je niet eerst apart de resultaten per model beschrijven voor je direct gaat vergelijken?
-> goed punt
T: Eerst worden alle XGBoost iteraties besproken, vervolgens alle DQN, later worden de beste modellen vergeleken in results

7.4 Stakeholder Evaluation ✅
- Veelbelovend. Je schrijft ook wat over DLL in de wiki. Ga door met ze en bespreek het gewoon. Je kan dat!
-> DLL is hem niet geworden
T: getest met fiscaal expert

8.1.4 Resource Demand ✅
- Interesting - but how would running (inference) the models in practice work out?
-> onrealistisch?
-> elaboration: als lezer wil ik een idee hoe lang dit zou duren in de praktijk. moet je elke keer zo lang leren? of is predicten veel sneller? gaat dat tegelijk? etc.
T: Ik bespreek inference times in vgm resource demand

8.2 Stakeholder Evaluation Results ✅
- Een combinatie van: 1) zelf toetsen aan wat ING / ABN AMRO hebben aangegeven in hun presentaties. 2) gesprek met DLL 3) wet-en regelgeving
-> goed punt
T: dit opgesplitst in industry insights met de bank presentaties en DLL veldonderzoek. En in prototype testen en evaluatie op design patterens

9. Discussie ✅
- Ook dit kun je. (referend naar het schrijven van H9)
-> komt goed
T: Discussie gescrheven

10. Conclusion ✅
- Hier moet je terugkomen op de hoofd en deelvragen en of deze nu beantwoord zijn. Dat zien we nu nog niet duidelijk genoeg.
-> komt goed
T: conclusie gescrheven