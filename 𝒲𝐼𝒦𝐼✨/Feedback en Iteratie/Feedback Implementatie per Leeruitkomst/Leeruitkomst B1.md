# Leeruitkomst B1 - Feedback en Implementatie

Hierin alle B1 feedback die ik heb ontvangen. Hiermee wil ik laten zien dat ik alle feedback die ik eerder heb gekregen in acht heb gehouden tijdens dit onderzoek. Dit is ook fijn voor mezelf om als checklist te gebruiken om eerdere fouten te voorkomen.

## Feedback:

### M&T-1a:


| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* Data is correct gesplitst</p> | Zie *1. Data Split* in [Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb) |
| <p>(+-)<br>* Je maakt geen gebruik van een stratisfied split, terwijl dat in deze situatie wel de conventie is. Waarom? | **[Dit wordt alleen hier besproken]** In mijn huidig onderzoek is het gebruik van stratification geen conventie. Ik heb nu een extreme class imbalance, dus dan zou je denken dat stratification een goed idee is. De dataset die ik gebruik heeft een chronologische volgorde. Dus als ik stratification zou gebruiken in deze dataset zou ik data leakage veroorzaken. Daarom kies ik er bewust voor geen stratification te gebruiken. Dit is nergens anders gedocumenteerd dan hier, aangezien ik dan net zo goed voor elk mogelijk techniek kan bespreken waarom ik het niet gebruik. |
| <p>(+-)<br>* Herschaling wordt niet verantwoord</p> | In mijn huidig onderzoek maak ik ook gebuik van herschaling. Nu bespreek ik wel de 2 meest gebruikte herschaalmethoden en kies ik de meest logische optie, zie *1.2 Preprocessing* in [DQN_v7.2.ipynb](../../../code/DQN/DQN_v7.2.ipynb) |
| <p>(-)<br>* Je laat tussentijds testresultaten zien. Pas hiermee op. Als je beslissingen hebt genomen naar aanleiding van deze resultaten, dan is er sprake van data-leakage.</p> | Data werd destijds gesplitst in 2 splits, train en test. In mijn huidig onderzoek split ik de data in 3 splits: train, val en test. Trainen op de trainset, tussendoors evalueren op de val set en na aanleiding van de resultaten op de valset beslissingen nemen. De testset wordt uitsluitend op het einde gebruikt wanneer ik niks meer verander, zie [XGBoost_v9.1.ipynb](../../../code/XGBoost/XGBoost_v9.1.ipynb) en [DQN_v7.2.ipynb](../../../code/DQN/DQN_v7.2.ipynb) |
| <p>(--)<br>* Je doet een dataverkenning op de gehele dataset (zonder splitsing). Dit is niet volgens de conventies en kan leiden tot data-leakage.</p> | De data verkenning wordt nu verricht op de train set, zie *2. Exploration* in [Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb) |

### Tech-Review Blok 1

| Feedback | Toepassing op dit Project |
|-|-|
| Drie datasets worden besproken. Jullie keuze wordt onderbouwd, uiteindelijk gekozen UTKFace, maar zijn jullie op de hoogte dat de leeftiijden niet echt zijn? | De transacties in mijn huidige dataset zijn ook synthetisch dit wordt besproken in mijn [Thesis](../../../rapport/) in *H5 Discussie* |
| Data preprocessing met YOLO en andere stappen is erg goed, complimenten. | Dit is allemaal behandeld in mijn [Thesis](../../../rapport/): Data Split (*3.3.2 Data Split*), Feature Engineering (*3.3.3*, *3.3.4* en *3.3.5*) en Data Preprocessing (*3.5.2 Reinforcement Learning: Deep Q-Network*) |
| Er is geen bewijs in het rapport dat de klassen goed zijn verdeeld en hoe groot de uiteindelijke dataset is.  DIt is wel besproken in de presentatie. | Data verdeling wordt duidelijk besproken in de EDA notebook ([Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb)) en kort samengevat in mijn [Thesis](../../../rapport/) in *3.3.1 Dataset Selection* |

### M&T-1b

| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* correcte splitsing</p> | **[Duplicate]** |
| <p>(-)<br>* normalisatie niet correct besproken</p> | Normalisatie wordt uitgevoerd en besproken. Zie *1.2 Preprocessing* in [DQN_v7.2.ipynb](../../../code/DQN/DQN_v7.2.ipynb) |

### Eindoplevering Project Blok 1

| Feedback | Toepassing op dit Project |
|-|-|
| <p>Datasetselectie is onderbouwd en vooral gebaseerd op project requirements.</p> | Dataset selectie is onderbouwd zie *3.3.1 Dataset Selection* in [Thesis](../../../rapport/) |
| EDA is zinvol ingezet. | EDA is uitgevoerd in [Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb) maar er zit niet persé data exploration in mijn thesis. |
| Wijze van data splitsing is aangegeven. | Wijze van data split wordt besproken in *3.3.2 Data Split* in [Thesis](../../../rapport/) |

### M&T-2a

| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* Splitsing correct gebruikt</p> | **[Duplicate]** |
| <p>(+)<br>* Voor- en nadelen van data besproken<br></p> | Zie *3.3.1 Dataset Selection* in [Thesis](../../../rapport/) |
| <p>(+)<br>* Voor- en nadelen van data gekoppeld aan model-kwaliteit, maar niet altijd correct verantwoord</p> | **[Dit wordt alleen hier besproken]** De data is tabular en geen graph data. Hierdoor is het moeiljik om relationele laundering patterns te detecteren waardoor het model dus moeite zal krijgen met bepaalde patronen. |
| <p>(+)<br>- Je zegt: "In NLP kan dit een voordeel zijn, áls je de betekenissen van de woorden in acht neemt." Waar is dat op gebaseerd?<br></p> | n.v.t. |
| <p>(+)<br>* Voor- en nadelen van data soms gekoppeld aan kwaliteit van het model en vertalingen, maar niet altijd<br></p> | **[Duplicate]** |
| <p>(+)<br>- Wat is het voordeel van een "diverse dataset"?</p> | n.v.t. |

### Tech-Review Blok 2

| Feedback | Toepassing op dit Project |
|-|-|
| <p>Ik heb dit (4.2) met plezier gelezen. Wat goed dat jullie ook vectordb's vergeleken hebben.En ik vind ook jullie chunking strategie goed (Dit heb ik nergens anders gezien vandaar boven niveau).</p> | n.v.t |

### M&T-2b

| Feedback | Toepassing op dit Project |
|-|-|
| <p>(+)<br>* data gesplitst</p> | **[Duplicate]** |
| <p>(+)<br>* correct stratisfied split verantwoord</p> | **[Duplicate]** |
| <p>(+-)<br>* Waarom maak je gebruik van een validatieset bij zo weinig data? Je had ook cv kunnen gebruiken.</p> | Originele boodschap is niet van toepassing hier want ik heb heel veel data, maar ik heb wel cross-validation overwogen. Zie *1. Data Split* in [Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb) |
| <p>(-)<br>* Je zegt dat je niet kan uitrekenen wat de kans is op dat je moet stratify-en en daarom simuleer je verschillende splits. Dat is een goede oplossing! Bedenk wel dat het niet nodig is om de gehele dataset te splitsen. Het gaat immers alleen om de aantallen van de labels. Om data-leakage te voorkomen had je ook zelf een dataset kunnen maken van 10 klasses in een specifieke verdeling om vervolgens te controleren hoe de verdelingen eruit zien na een willekeurige split. Leuk!</p> | n.v.t. (Leuk om enthousisasme te lezen in de feedback ❤️) |
| <p>(--)<br>* Wees voorzichtig met het bekijken van de data. Hoe weet je dat je niet al naar de testdata hebt gekeken?</p> | Ik heb de verkenning toegepast op de trainset. ik kijk wel naar de target variable verdeling op elke set, dit is om er zeker van te zijn dat er voldoende suspicious cases zijn in elke split. Zie *2. Data Exploration* in [Data_Exploration_and_Preperation_v1.7.4.ipynb](../../../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb) |
| <p>(--)<br>* Je lijkt elke keer opniew de MNIST-data in te laden via keras.datasets.mnist.load_data(), maar dat was niet de opdracht.</p> | n.v.t. |

### Eindoplevering Project Blok 2

| Feedback | Toepassing op dit Project |
|-|-|
| De gekozen data is passend voor de taak. | Ja, Zie *3.3.1 Dataset Selection* in [Thesis](../../../rapport/) |
| Data-analyse is beperkt uitgevoerd. | De data analyse is nogmaals aan de zwakkere kant. |
| Splits zijn toegelicht | Splits worden toegelicht in *3.3.2 Data Split* in [Thesis](../../../rapport/) |
| Wijze van sampling is aangegeven | n.v.t. |
| rekening gehouden met imbalance. | ja, d.m.v. AUPRC als evaluatie-metric. Zie *3.4 Evaluatie Metric* in [Thesis](../../../rapport/) |
| Beperkingen zijn aangestipt. | Ja zie *H5 Discussie* in [Thesis](../../../rapport/) |

### Onderzoeksplan

| Feedback | Toepassing op dit Project |
|-|-| 
| <p>Je werkt met een synthetische dataset; je legt te weinig verantwoording af of dit representatief is voor de NL situatie.</p> | ik leg uit dat de gekozen dataset niet representatief is in *H5 Discussie* in [Thesis](../../../rapport/). Ook leg ik uit dat de dataset die representatief is te weinig volume heeft in *3.3.1 Dataset Selection* in [Thesis](../../../rapport/). Vandaar dat ik toch de niet-representatieve dataset kies. Ook al kies ik alsnog een niet representatieve dataset ben ik nu wel bewust van de keuze |

### M&T-3a

| Feedback | Toepassing op dit Project |
|-|-| 
| <p>(+)<br>* keuze minimaal aantal ratings per gebruiker of film verwoord en verantwoord<br></p> | n.v.t. |
| <p>(+)<br>* Enkele voor- en nadelen worden besproken<br></p> | **[Duplicate]** |
| <p>(+)<br>* Nuttige statistieken (Scheve verdeling, long tail, sparsity)</p> | Alle notebooks bevatten nuttige statistieken die ook terug komen in mijn thesis. Zie [Notebooks](../../../code/) |
