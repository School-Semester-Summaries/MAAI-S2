Feedback Comments in "Master_Thesis_KG_v0.1_70perc-KvM.pdf" op  "Master_Thesis_KG_v0.1.pdf", including elaboration.
- Status: Alle Feedback Toegepast ✅

Terminology:
F = Feedback
-> = Mijn reactie/notitie op de feedback
F2 = Dezelfde feedback maar dan elaborated
T = Toepassing van de feedback
✅ = voldaan

1.2.1 ✅
- F: Waarom zeg je niets over de derde en vierde plaats?
- -> Die hebben hun code niet gedeeld
- F2: mention ook nog impliciet dat derde en vierde plaats niet gedeeld hebben
- T: Het stukje boven de vergelijking aangepast: 

Van
> *"An analysis of the top-performing teams (which shared their solution) reveals a heavy reliance on supervised learning, specifically Gradient Boosting Decision Trees (GBDT):"*

Naar
> *"Of the five top performing teams, three publicly shared their solutions. An analysis of these reveals a heavy reliance on supervised learning, specifically, Gradient Boosting Decision Trees (GBDT):"*

1.5 Research Question ✅
- F: De huidige vraag kan worden beantwoord met JA of NEE. Misschien kun je de vraag herformuleren: To what extent .......
-> Prima
- T: De onderzoeksvraag veranderd:

Van
> *"Can Reinforcement Learning effectively detect money laundering, and how does it compare to leading supervised learning methods on transaction data?"*

Naar
> *"To what extent can Reinforcement Learning effectively detect money laundering, and how does it compare to leading supervised learning methods on transaction data?"*

2.2 Related Work Comparison ✅
- F: Waarom beperk jij je tot RL only? Waarom kies je niet voor GNN + RL Graag je keuze motiveren/onderbouwen.
-> Waarom kies ik niet 100 miljoen andere technieken waar zich nu een gat in de kennis in bevind. ik heb RL gekozen omdat ik dat interessant vind, en heb aangetoond dat RL only en GNN + RL beide een gat in de kennis bevatten. Ik heb ervoor gekozen om RL only te kiezen omdat Rainesh al het andere doet en lijkt me niet leuk om allebei het zelfde te kiezen. het lijkt me ook niet nodig om meer verantwoording af te leggen dan dit. De kunst ligt namens mij meer in het aantonen dat er een gat in de kennis bestaat.
- F2: motiveer ergens waarom je de modellen kiest die je hebt gekozen,
- -> 1.4 kritisch doornemen: is het logisch waarom ik kies voor RL, en is het logisch waarom ik niet kies voor RL+GNN
- T: 1.6 Scope en 1.5 Research Questions omgewisseld in mijn scriptie. Nu is 1.5 Scope en 1.6 Research Questions. Hoofdstukken: 1.4 Identified Gap, 1.5 Scope & 1.6 Research Questions herschreven.


3 Research Design ✅
- in hoofdstuk 3 zou je zo concreet mogelijk moeten aangeven wat je gaat doen: welke modellen ga je gebruiken, welke performance metrices ga je gebruiken (en waarom is voor deze metrices gekozen), etc...
-> Prima
- T: Hoofdstuk 3 heet nu Methodology en de hoofdstukken Data (H5), Evaluatie (H7) en Modellen (H6) zijn nu deel van hoofdstuk Methodology. Methodology ziet er nu zo uit:

Van
> 3. Research Design
> - 3.1 Research Design
> - 3.2 Type of Study
> - 3.3 Baseline Definition
> - 3.4 Comparison Logic
> 4. Requirements
> - 4.1 Legal & Ethical Requirements
> - 4.2 Functional Requirements
> - 4.3 Technical Requirements
> 5. Data
> - 5.1 Data Sources
> - 5.2 Data Characteristics
>   - 5.2.1 Features
>   - 5.2.2 Class Imbalance
>   - 5.2.3 Train/Test Split
> - 5.3 Preprocessing
> - 5.4 Data Risks
> - 5.5 Bias Consideration
> 6. Model & Architecture
> - 6.1 Model Selection
>   - 6.1.1 Baseline: XGBoost
>   - 6.1.2 Reinforcement Learning Model: DQN
> - 6.2 Model Overview
> - 6.3 XGBoost: Architecture & Tuning
>   - 6.3.1 Fixed Configuration
>   - 6.3.2 Iteration 1: Baseline
>   - 6.3.3 Iteration 2: Grid Search
> - 6.4 DQN: Architecture & Tuning
>   - 6.4.1 MDP Formulation
>   - 6.4.2 Network Architecture
>   - 6.4.3 Training Mechanics
>   - 6.4.4 Iteration 1: Baseline
>   - 6.4.5 Iteration 2: Scaled Hyperparameters
> - 6.5 Observed Trade-offs
> 7. Evaluation
> - 7.1 Evaluation Metric
> - 7.2 Validation Strategy
> - 7.3 Baseline Definition
> - 7.4 Stakeholder Evaluation

Naar
> 3. Methodology
> - 3.1 Research Overview
> - 3.2 Type of Study
> - 3.3 Requirements
>   - 3.3.1 Legal & Ethical Requirements
>   - 3.3.2 Functional Requirements
>   - 3.3.3 Technical Requirements
> - 3.4 Data
>   - 3.4.1 Dataset Selection
>   - 3.4.2 Data Split
>   - 3.4.3 Feature Engineering — Iteration 1: Raw Features
>   - 3.4.4 Feature Engineering — Iteration 2: Account-level Aggregates
>   - 3.4.5 Feature Engineering — Iteration 3: Pair History
> - 3.5 Evaluation Metric
> - 3.6 Models
>   - 3.6.1 Baseline Definition: XGBoost
>     - Iteration 1: Default hyperparameters
>     - Iteration 2: Grid Search
>     - Iteration 3: Bayesian Optimisation
>   - 3.6.2 Reinforcement Learning: Deep Q-Network
>     - Data Preprocessing
>     - MDP Formulation
>     - Network Architecture
>     - Training Mechanics
>     - Iteration 1: Lin et al. reward function (λ = ρ)
>     - Iteration 2: Zhinin-Vera et al. reward function (λ = 0.1)
>     - Iteration 3: Adjusted epsilon decay
>     - Iteration 4: Dropout regularisation
>     - Iteration 5: Reduced dropout rate (p = 0.2)
>     - Iteration Summary


7.1 ✅
- De keuze van de performance metrices moeten eerder in dit verslag worden besproken en onderbouwd
-> prima
- T: wordt nu besproken in de inleiding van H3 en besproken na data voor modellen en resultaten.

7.4 Stakeholder Evaluation ✅
- Aandachtspunt voor rubrics
-> ok
T: Tested the design patterns with a financial expert. This is documented in wiki [Prototype Testing](../../Onderzoek/Prototype%20Testen/README.md)

8.1.1 Performance ✅
- Je zou ook iets moeten zeggen over de hyperparameters. en de tussenresultaten van de verchillende stappen van de analyses.
-> Prima (dit staat in de notebooks gwn overnemen)
T: Iteraties en tussenresultaten worden besproken in 3.6 Models

- Wellicht is het ook informatief om ook precision en de recall te vermelden in tabel 16 ✅
-> de precision en recall wordt uitgerekend voor elke mogelijke threshold, dus dat gaat moeilijk.
-> elaboration: leg uit dat het AUPRC wordt gebruikt om te peilen hoe goed het model is. vervolgens bij het testen kan de expert vaststellen welke waarde mogelijk en gewenst is voor de desbetreffende organisatie.
T: in de prototype kun je de threshold wijzigen, precision of recall tot een waarde brengen. Ook wordt benoemd in evaluation metrics dat we geen vaste threshold gebruiken en dat deze threshold moet vastgesteld worden in de prototype op basis van medewerker count

8.1.2 Explainability ✅
- Je zou in een appendix de betekenis van de verschillende features moeten aangeven.
-> eens
T: Feature overview staat nu in de appendix

8.2 ✅
- Aandachtspunt voor rubrics op Brightspace
-> ok
T: verwerkt bij prototype en design patterns (er is een kans dat dit naar de appendix wordt geplaatst)

10.3 ✅
- F: Paragraaf 10.3 lijkt mij niet relevant voor je eindrapport
- T: Verwijderd uit thesis


Wat kan in de Appendix?
- grote tabellenverzameling, 
- dingen die dieper uitgelegd kunnen worden
- dingen die in de hoofdtekst de leesbaarheid verziekt
