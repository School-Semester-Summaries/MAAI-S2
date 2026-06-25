# Leeruitkomst B2 - Feedback en Implementatie

Hierin alle B2 feedback die ik heb ontvangen. Hiermee wil ik laten zien dat ik alle feedback die ik eerder heb gekregen in acht heb gehouden tijdens dit onderzoek. Dit is ook fijn voor mezelf om als checklist te gebruiken om eerdere fouten te voorkomen.

## Feedback:

### M&T-1a


| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* Correcte verantwoording van nulmodel</p> | **[Dit wordt alleen hier besproken]** ik heb geen nulmodel gebruikt. ik leg nergens uit waarom maar je kunt het logischerwijs herleiden uit het feit dat een nulmodel geen waarde toevoegt aan mijn onderzoek. Ik heb een extreem imbalanced dataset. Mocht je alle transacties suspicious beoordelen of juist niet suspicious beoordelen behaal je hier geen interesante resultaten mee. Je krijgt of: een extreem hoge accuracy, perfecte recall, extreem lage precision en een extreem lage AUPRC. Daarom maak ik gebruik van een baseline model en probeer ik dat model te verbeteren. |
| <p>(-)<br>* Prestatiemaat wordt niet correct verantwoord</p> | Prestatiemaat AUPRC/AUCPR wordt voldoende verantwoord, maar niet binnen de notebooks. Zie *3.4 Evaluation Metric* in [Thesis](../../../rapport/). |
| <p>(-)<br>* Het is onduidelijk uit welke modellen je gekozen hebt.</p> | Nu is dat wel duidelijk, maar niet binnen de notebooks. Zie *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |
| <p>(-)<br>* De keuze van het model is niet logisch (KNN werk niet goed bij veel waarnemingen) | n.v.t. |
| <p>(-)<br>* Verantwoording voor het model is niet overtuigend. Er zijn heel veel modellen die aan dat argument voldoen (classificatie en "een keer gehoord") | n.v.t. (de booschap die ik hieruit kan halen is dat mijn verantwoording erg zwak was en niet gebasseerd op literatuur. Dat is nu wel het geval) |
| <p>(-)<br>* Je besluit een variabelenselectie te gebruiken. De keuze voor de methode wordt niet verantwoord</p> | Ik maak een variabelenselectie in mijn grid search experiment. Ik verantwoord de keuze voor de gekozen variabelen in de grid search, Zie *Iteration 2 - Grid Search* in [XGBoost Notebook](../../../code/XGBoost/XGBoost_v9.1.ipynb). Echter leg ik niet uit waarom ik grid search kies, ik zag dit meer als een logische eerste keuze. | 


### Tech-Review Blok 1

| Feedback | Toepassing op dit Project |
|-|-|
| Ik merk dat ik jullie hier kwijt raak. ResNet en VGG lopen in mijn beleving door elkaar. Een goede introductie bij 4.3(.1) kan al veel verhelpen. De uitwerking van de modellen is dan weer prima gedaan. | De iteraties van XGBoost en DQN worden beided apart besproken. Zie *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |

### M&T-1b

| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* nulmodel correct verantwoord</p> | n.v.t. **[Duplicate]** |
| <p>(+)<br>* geschikte architectuur gedeeltelijk gerelateerd aan f(x)</p> | DQN architectuur gebasseerd op de literatuur, Zie *2. DQN Architectuur* in [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb). Alhoewel de architectuur gebasseerd is op de literatuur, vind ik dit persoonlijk toch een minder sterke keuze aangezien de data volume van de paper waarop de architectuur is gebasseerd niet vergelijkbaar is. |
| <p>(+-)<br>* Keuze van activatiefunctie niet helemaal overtuigend. We willen de functie f(x) die uit tanh's is opgebouwd zien te benaderen. Je had gebruik mogen maken van die informatie.</p> | architectuur inclusief activatie functie gekopierd uit de literatuur. Zie *2. DQN Architectuur* in [DQN Notebook](../../../code/DQN/DQN_v7.2.ipynb). | 
| <p>(-)<br>* Foutmaat niet correct verantwoord. Je zegt: "aangezien MAE beter presteert dan MSE als er ruis is". Waar is dat op gebaseerd? Wat betekent dit precies? In deel 3 ga je hier verder op in: "omdat MAE grote outliers met een korrel zout neemt terwijl MSE het zoveel mogelijk probeert mee te nemen in de lijnvorm". Dit is niet echt precies verwoord, maar komt al dichter in de buurt van de werkelijkheid. De MSE en de MAE zullen anders omgaan met uitschieters. Wat heeft dat te maken met of er ruis is of niet?</p> | Prestatiemaat is duidelijk verantwoord, maar niet in notebook. Zie *3.4 Evaluation Metric* in [Thesis](../../../rapport/). |

### Eindoplevering Project Blok 1

| Feedback | Toepassing op dit Project |
|-|-|
| Vanuit literatuur onderbouwde architectuurkeuze. | DQN Architectuur volgt liteatuur. Zie *3.5.2 Reinforcement Learning: Deep Q-Network* in [Thesis](../../../rapport/). Alhoewel de architectuur gebasseerd is op de literatuur, vind ik dit persoonlijk toch een minder sterke keuze aangezien de data volume van de paper waarop de architectuur is gebasseerd niet vergelijkbaar is. |
| Loss-functie toegelicht | Architectuur inclusief loss-function gebasseerd op literatuur. Zie *3.5.2 Reinforcement Learning: Deep Q-Network* in [Thesis](../../../rapport/). |
| wijze van minimaliseren overfitting toegelicht | Overfitting wordt voorkomen door early stopping. Bij de DQN is overfitting op de train set een probleem. Iteraties 3, 4 en 5 proberen dit op te lossen. Zie *3.5.2 Reinforcement Learning: Deep Q-Network* in [Thesis](../../../rapport/). |
| Hyperparameters gegeven | Hyperparameters in beide modellen gebaseerd op literatuur. Zie *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |
| Evaluatie toegelicht | Modellen worden geëvalueerd op alle criteria van leeruitkomst C2 behalve scalability. Zie *H4 Results* in [Thesis](../../../rapport/) |
| Evaluatiemetrieken toegelicht | Zie *3.4 Evaluation Metric* in [Thesis](../../../rapport/).  |
| niet sterk gerelateerd aan literatuur | Nu wel |

### M&T-2a

| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* Keuze van prestatiemaat is verantwoord. Je hebt correct besproken dat dit niet de logische keuze is en dat de literatuur iets anders suggereert.</p> | **[Duplicate]** |
| <p>(-)<br>* Eerste iteratie is verantwoord (met bron) en deels gerelateerd aan de specifieke situatie</p> | Alle iteratie worden gelinkt aan literatuur. Zie [Notebooks](../../../code/). |
| <p>(-)<br>- De bron suggereert dat de vocabulary 20 duizend tokens zou moeten bevatten | n.v.t. |
| <p>(-)<br>- De bron suggereert niet dat n-grams nuttig zouden zijn in een sequence-model. Dit is wat ongewoon en zou echt beter verantwoord moeten worden. Standaard is juist dat je kiest tussen een sequence-model of een set-model met N-grams</p> | n.v.t. (de boodschap die je hieruit kunt halen is dat ik de geciteerde literatuur goed begrijpend moet lezen) |

### Tech-Review Blok 2

| Feedback | Toepassing op dit Project |
|-|-|
| Dit is goed uitgevoerd. Het plaatje fig 6 op p 20 helpt maar een UML diagram &nbsp;(zoals bijv, sequence diagram) zou nog beter zijn. | n.v.t. (van toepassing bij complexere pipelines) |
| Ik vind jullie naive RAG keuze prima en ook dit heb ik met plezier gelezen. | n.v.t. |
| Alleen de leesplank-noot modellen zijn beschreven. Zijn er nog andere modellen bekeken of beoordeeld? Op Huggingface ca. 2 miljoen modellen... | Ik bespreek supervised modellen in *1.2 Literature Overview* en *1.3 Industry Insights*, en RL modellen in *1.4 Identified Gap* en *2.2 Related Work Comparison* |
| Beschrijf globaal &nbsp;(mag ook in bijlage) hoe je tot deze keuze gekomen bent. Bekijk bijv de architectuur (encoder / decoder / encoder-decoder ) welke geschikt is voor deze taak van 'vertalen' van moelijk naar simpele tekst. &nbsp; | Verantwoording is gedocumenteerd in *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |
| Bestudeer ook &nbsp;benchmarks of maak een LLM Arena, vergelijk meerdere modellen op de test/val set en zie hoe ze scoren. Wil je bij de eindbeoordeling een op-niveau halen dan moet je hier verder naar kijken. | **[Dit wordt alleen hier besproken]** een LLM arena had uitgevoerd kunnen worden op de supervised modellen die voorkomen in AML literatuur. Anderzijds, is het maar de baseline model dus is het niet dermate van belang, maar het had de baseline keuze wel sterker gemaakt. |

### M&T-2b

| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* Model uit slides als basismodel VAE gebruikt</p> | n.v.t. |
| <p>(+)<br>* Basismodel (voor classificatie) is gekozen en logisch&nbsp;</p> | Feedback refereert naar een minimalistische CNN. Dit komt terug in mijn onderzoek. Bij het XGBoost model begin ik in de eerste iteratie met een zo minimalistich model met zoveel mogelijk default waarden. |
| <p>(-)<br>* Prestatiemaat is impliciet gegeven en niet verantwoord</p> | **[Duplicate]** |

### Eindoplevering Project Blok 2

| Feedback | Toepassing op dit Project |
|-|-|
| <p>In combinatie met de bijlagen is de&nbsp; architectuur toegelicht en zijn keuzes onderbouwd.</p> | **[Duplicate]** |

### Onderzoeksplan (Teams Meeting + DLO)

| Feedback | Toepassing op dit Project |
|-|-| 
| Bespreek eveneens literatuur over de supervised modellen waarmee je RL zou kunnen vergelijken. (Comment uit [Kaan_PvA_AML_v2-KvM.pdf](./PvA/Kaan_PvA_AML_v2-KvM.pdf)) | ik bespreek nu 3 onderdelen voor supervised methodes, de competitie, de comparison paper, en de banken die beide xgboost gebruiken. Zie *1.2 Literature Overview* en *1.3 Industry Insights* in [Thesis](../../../rapport/) |
| benoem expliciet dat dit aansluit op mijn casus. voor welke situatie hebben zij precies toegepast. welke subtak wordt er op gefocust binnen 6 en 17. benoem dit. (Interpretatie uit [Aantekeningen feedback-gesprek met Kees](./PvA/Kaan_PvA_AML_v2%20-%20Feedback.txt)) | Ik benoem nu dat de paper dqn gebruikt voor het detecteren van credit card fraud in the context van transaction monitoring. Zie *1.2.2 Reinforcement Learning, an Emerging Method* in [Thesis](../../../rapport/) |
| Zie paragraaf 2.1, 2.2, 2.3, 3.1, 3.2, 3.3 en 3.4. | n.v.t. (dit is een manier om aan te tonen dat B2 voldoende is met als bewijs deze paragraven) | 

### M&T-3a

| Feedback | Toepassing op dit Project |
|-|-| 
| <p>(+)<br>* Iedereen krijgt drie aanbevelingen</p> | n.v.t. (je kunt dit interpreteren als, de opgestelde requirements zijn nagevolgd) |
| <p>(+)<br>* De keuze wanneer je een persoon een persoonlijke of niet-persoonlijke waardering geeft, is helder verantwoord&nbsp;</p> | n.v.t. |
| <p>(+-)<br>* Keuze voor baseline-model van waarderingsmodel niet helemaal duidelijk. Wat als iemand zo een populaire film al heeft gezien? Aha! Dat leg je later wel uit.</p> | n.v.t. |
| <p>(-)<br>* Geen verantwoording voor het waarderingsmodel (SVD) in de eerste iteratie</p> | Gekozen modellen zijn verantwoord, maar niet in de notebooks. Zie *3.5.1 Baseline Definition: XGBoost* en *3.5.2 Reinforcement Learning: Deep Q-Network* in mijn [Thesis](../../../rapport/). |

### M&T-3b

| Feedback | Toepassing op dit Project |
|-|-| 
| <p>(+) Gestructureerde beschouwing van mogelijk modelkeuzes met bijbehorende voor- en nadelen, grotendeels toegespitst op het probleem dat opgelost moet worden.</p> | **[Dit wordt alleen hier besproken]** De gestructureerde beschouwing refereert naar de vergelijking tussen 16 algortimes. In mijn thesis doe ik geen vergelijkbaar gestructureerde beschouwing per beschikbaar model. Voor XGBoost is dit niet perse nodig omdat XGBoost het baseline model is en veel literatuur hint naar XGBoost. Voor het gekozen RL algortime was het zeker een goed idee geweest. Nu is er voor DQN gekozen omdat een paper dqn gebruikt maar dat is niet bepaald sterk. Ook zou het erg waardevol zijn om zelf deze gestructureerde analyse uit te voeren puur omdat er dus zo weinig research naar gedaan is. |
| <p>In bovenstaande analyse maak je wel een aantal fouten waardoor je op Q-learning uitkomt terwijl dit niet de optimale keuze is:</p> | n.v.t. (nu heb ik zonder analyse DQN gekozen, maar in retrospect weet ik niet of dit de correcte keuze is). |
| <p>(-) Je schrijft: "<em>Experience replay is waardevol voor Acrobot omdat de omgeving veel episodes vereist voordat een goede policy ontstaat, dit baseer ik op het feit dat de gemiddelde step lengte voor completion 2015 steps is met mijn baseline.</em>" De lengte van een enkele episode onder een random policy heeft niks te maken met hoeveel episodes je nodig hebt om te leren.</p> | n.v.t. (Zeer scherpe evaluatie, nice!) |
| <p>(-) Maak gebruik van de reward structuur van AcroBot in je argumentatie voor modelkeuze. Q-learning maakt gebruik van de ontvangen beloning in een enkele tijdstap, deze is hier constant -1 en bevat dus nogal weinig informatie om uit te leren. De echte informatie zit in wanneer de episode eindigt, dus je wilt juist van volledige episodes leren.&nbsp;</p> | n.v.t. | 
