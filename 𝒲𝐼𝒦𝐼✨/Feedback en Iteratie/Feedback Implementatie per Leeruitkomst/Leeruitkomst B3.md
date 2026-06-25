# Leeruitkomst B3 - Feedback en Implementatie

Hierin alle B3 feedback die ik heb ontvangen. Hiermee wil ik laten zien dat ik alle feedback die ik eerder heb gekregen in acht heb gehouden tijdens dit onderzoek. Dit is ook fijn voor mezelf om als checklist te gebruiken om eerdere fouten te voorkomen.

## Feedback:

### M&T-1a:


| Feedback | Toepassing op dit Project |
|-|-|
| <p>(-)<br>* Niet van alle hyperparameters wordt de keuze verantwoord (ook "default" is een keuze)</p> | Nu wel, zie [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb) |


### Tech-Review Blok 1

| Feedback | Toepassing op dit Project |
|-|-|
| Er zijn meerdere iteraties uitgevoerd. | Nu ook, zie *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |
| Er is literatuur gezocht en besproken, complimenten. | Nu ook, zie *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |
| Maar omdat ik bij B2 het overzicht al kwijtgeraakt was, loop ik hier verder vast. | n.v.t. |


### M&T-1b

| Feedback | Toepassing op dit Project |
|-|-|
| <div class="html-feedback"><p>(+)<br>* Het onderzoekje naar learning rate (LR) is goed, maar misschien te gedetailleerd en op het verkeerde moment. Je zou wil liever niet achteraf op zoek naar de beste LR, maar vanaf het begin. Zeker als je veel grotere modellen gaat trainen (waar je niet de tijd hebt om zoveel opties af te gaan). Voor de LR is het vooral van belang dat je erachter komt wat de juiste orde van grootte is. Dus 0,1 of 0,01 of 0,001 etc.. Het verschil tussen 0,045 en 0,040 is niet echt van belang (en neemt teveel tijd in beslag).</p> | learning rate wordt logischerwijs onderzocht met gebruik van grid search in *Iteration 2 - Grid Search* in [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb). Gekozen waarden worden onderbouwd door de literatuur. Vervolgens neem ik een stap verder en pas ik bayesian optimization toe om nauwkeuriger te zoeken naar de optimale waarde, zie *Iteration 3 - Bayesian Optimization* in [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb). |
| <p>(+-)<br>* Je schrijft in deel 3: "Om zeker te weten dat mijn model niet overfit is, predict ik ook de validatie set.". Dat is inderdaad verstandig. Is het mogelijk om in deze situatie (complexiteit van model en aantal waarnemingen) te overfitten?</p> | n.v.t. |
| <p>(-)<br>* Je merkt terecht op dat early-stpoping een goed idee zou zijn geweest bij zo een groot aantal epochs. Probeer jezelf aan te leren dat standaard te doen (of misschien nog beter: begin met een klein aantal epochs om te contrroleren of alles wel werkt en of er geleerd wordt). In het vervolg van de opleiding worden de modellen en de rekentijd groter (veel groter) en is er geen tijd om te wachten op 50.000 epochs.</p></div> | early stopping toegevoegd aan beide modellen in elke iteratie, zie [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb) |
 
### Eindoplevering Project Blok 1

| Feedback | Toepassing op dit Project |
|-|-|
| Systematische verfijning helder en gedetailleerd in 4 iteraties beschreven. | **[Duplicate]** |

### M&T-2a

| Feedback | Toepassing op dit Project |
|-|-|
| (+)<br>* Basismodel werkend gekregen | In dit onderzoek is XGBoost het basismodel en die werkt. |
| (+)<br>* Verschillen met model uit slides besproken | ik interpreteer dit als: kan de student het verschil tussen iteraties documenteren. Ja, zie de verantwoording per iteratie in [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb) |
| (+)<br>* Eerste iteratie is uitgevoerd | ja, voor beide modellen, zie [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb) |
| <p>(+-)<br>* Tweede iteratie is verantwoord en gerelateerd aan resultaten, maar is wel een vreemde suggestie. N-grams combineren met een sequence-model is niet standaard. Heb je hier literatuur bij gevonden?</p> | Elke iteratie is verantwoord, zie [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb) |
 

### Tech-Review Blok 2

| Feedback | Toepassing op dit Project |
|-|-|
| De systematische aanpak is beschreven onder 8.2. | Aanpak beschreven in *3.1 Research Overview* in [Thesis](../../../rapport/) | 
| In de presentatie kwam het toekomstig werk goed naar voren. | Ik benoem toekomstig werk in *5.2 Evaluation of Design Choices* in [Thesis](../../../rapport/) |
| Voor eindbeoordeling herschrijven. | n.v.t. |
 

### M&T-2b

| Feedback | Toepassing op dit Project |
|-|-|
| (+)<br>* Hoge test-core behaald, maar verantwoording van iteraties is niet helemaal duidelijk. | **[Duplicate]** |
| (+)<br>* Helder stappenplan waarin je de volgorde van de iteraties bespreekt | **[Duplicate]** |
| (+)<br>* De meeste iteraties van de VAE zijn verantwoord (gebaseerd op de resultaten) | **[Duplicate]** |
| (+-)<br>* Je bespreekt correct het voordeel van het vergoten van de latente ruimte, maar bespreekt niet het nadeel voor de classifier en de hoeveelheid gelabelde data | Ik interpreteer dit als: verantwoor de voor- en nadelen voor beide modellen bij een designkeuze. Ik benoem dat de feature engineering voornamelijk gefocust was op het optimaliseren van XGBoost. Maar bespreek ook dat dit een nadeel kan zijn voor de DQN. Zie *5.2 Evaluation of Design Choices and Iterations* in [Thesis](../../../rapport/) |
| (-)<br>* Je doet een grid-search op de dimensie van de latente ruimte. Waarom kies je die waarden? | Grid search waarden worden nu wel verantword, zie *Iteration 2 - Grid Search* in [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) |
| (-)<br>* Je hertraint vaak hetzelfde model om de variatie in prestatie te meten. Waarom je dit wil (en daar zoveel rekenkracht aan besteed) is niet duidelijk.<br> | n.v.t. |
| (-)* Complexiteit van het model wordt niet besproken (hoeveel parameters versus hoeveel waarnemingen?)</p> | Model complexity wordt besproken in *4.2.3 Model Complexity* in [Thesis](../../../rapport/) |
 
### Eindoplevering Project Blok 2

| Feedback | Toepassing op dit Project |
|-|-|
| Proces is duidelijk | **[Duplicate]** |
| iteraties bouwen door op voorgaande. | **[Duplicate]** |
| Toelichting op de iteraties is helder en de stappen zijn logisch | **[Duplicate]** |
 

### M&T-3a

| Feedback | Toepassing op dit Project |
|-|-| 
| (-)<br>* Geen bespreking van de hyperparameters | Hyperparameters worden besproken, zie [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb) |
| (-)<br>* Vervolgstap helder verantwoord, maar niet gebaseerd op resultaten en iets wat je van tevoren ook had kunnen bedenken. | **[Dit wordt alleen hier besproken]** Op basis van de resultaten van de DQN in iteraties 1 tot en met 5, zou ik gaan kijken of het veranderen van de architectuur het model kan verbeteren. |
| (-)<br>* Je stelt voor om de opdracht aan te passen (gebruikers niet meenemen). Dat kan natuurlijk, maar houd dan ook altijd rekening met de opdrachtgever. De opdrachtgever hoort de opdracht goed te keuren (en zal dat alleen doen als zijn/haar "probleem" wordt opgelost. | n.v.t. (Goed punt) |
 

### M&T-3b

| Feedback | Toepassing op dit Project |
|-|-| 
| <p>(-) In iteratie 1 zie je nauwelijks verbetering van prestaties over 100 episodes, de plot van rewards vlakt af (en heeft veel ruis...), waarom zou je verwachten dat dit wel na 250 episodes gaat gebeuren?</p> | **[Duplicate]** (Goed punt, achteraf gezien inderdaad een vrij vreemd en luie iteratie en welverdiend onder niveau) |
 
