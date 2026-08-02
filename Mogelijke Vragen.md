**Mogelijke Vragen:**

\- Wat is het verschil tussen Layering en Integration?

\- Wat was precies het doel in de IEEE-CIS FD competitie?

&#x20;> Een model trainen om de variabel isFraud te voorspellen, gebruikmakend van AUC-ROC

\- Aangezien de IEEE-CIS FD competitie een fraude detectie competitie is, is het dan niet zwak om dit te gebruiken als beargumentering voor je modelkeuze?

&#x20;> De competitie sluit inderdaad niet 1 op 1 aan op mijn scenario, maar het heeft wel overlap. Zo wordt in beide cases een kans geschat hoe waarschijnlijk het is dat een transactie fraudelent is. De competitie op zich zou een zwakke verantwoording zijn. Maar zie het meer als aanvullende verantwoording in combinatie met industry practise en de survey paper.

\- Waarom staat de Youssef et al. tabel niet in de paper?

&#x20;> Erg grote tabel. Dit stuk is geschreven voordat ik had besloten gebruik te maken van een appendix. Bij nader inzien paste het mooi in de appendix maar daar heb ik niet meer aan gedacht.

\- Hoe kan het dat in jouw onderzoek XGBoost RL compleet outperformt maar in de FraudGNN-RL paper dit andersom blijkt te zijn?

&#x20;> Dit heeft hoogstwaarschijnlijk te maken met het feit dat ik mijn features heb geëngineerd in een iteratief proces op een XGBoost model. Tot mijn kennis heeft cui et al. geen enkele vorm van feature engineering laat staan op een xgboost model. Dit kan verklaren waarom het xgboost model niet domineert in tegenstelling tot mijn onderzoek

\- wat bedoel je met "The only pure RL approach"?

&#x20;> Het enige onderzoek waarbij RL zonder combinatie met een andere techniek is gebruikt in een vegelijkbare context

\- Waarom een focus op tabular data? Kunnen bedrijven hun tabular data niet omzetten in graph data?

&#x20;> Dat klopt, een graph zou prima te bouwen zijn met sender/receiver/tijd. Beide tabular en graph-based approaches zijn in de context van AML nog niet onderzocht. Omdat RL op tabular data de simpelere aanpak is, wilde ik dit onderzoeken om zo bij te dragen aan de literatuur.

\- Waarom meteen DQN en niet een simpelere RL techniek?

&#x20;> De literatuur toonde aan dat DQN al meerdere keren onderzocht binnen gerelateerde context. Maar ik kan me voorstellen dat dat opzich niet perse voldoende verantwoording is. Dus heb ik de RL tabel van de les ingevuld om zo te komen tot de ideale RL algoritme -> **Tabel komt in de presentatie**

\- Why no Cryptodatasets?

&#x20;> This research focusses on real banks and real banking data specfically. Even though the data is synthetic it is still based on real banking data.

\- How is sub-question 1 answered?

&#x20;> With the markov decision formulation

\- How is sub-question 2 answered?

&#x20;> Chapter Results

\- How is sub-question 3 answered?

&#x20;> Chapter Discussion

\- Waarom SHAP in plaats van andere alternatieven?

&#x20;> SHAP werd besproken in de literatuur en is industry practise.

\- Heb je alternatieven bekeken?

&#x20;> Heel kort, ik weet dat er alternatieven bestaan waarvan de meest interesant alternatief uit mijn hoofd Lime is. aangezien je daarmee ook individuele transacties kunt uit laten leggen door blackbox modellen. Maar omdat de literatuur en industry practise al naar SHAP hinten heb ik er niet al te lang bij stil gestaan.

\- Je zegt dat SAML-D gekozen is boven IBM omdat IBM typologies niet uitlegt, maar IBM legt de typologies wel uit?

&#x20;> Dat is waar, hier ben ik zelf later achter gekomen. Hierdoor wordt IBM bijna een gelijkwaardige keuze ten opzichte van SAML-D, de andere reden om SAML-D te kiezen blijft staan namelijk dat het meer typologies heeft.

\- Hoe werkt pair\_tx\_count bij een cash deposit of een cash withdrawal? aangezien dit dan toch naar de bank gaat?

&#x20;> dan is de receiver account inderdaad de desbetreffende geldautomaat

\- je zegt getraind op 12 raw features maar dit zou betekenen dat je de labels ook hebt meegnomen aangezien 2 van de 12 raw features labels zijn?

&#x20;> Dit is een schrijffout het zouden 10 raw features moeten zijn

\- Heb je andere evaluatie criteria overwogen.

&#x20;> Nee, literatuur en voornamelijk industry practise tonen beide duidelijk aan dat AUPRC de meest geschikte keuze is.

\- Heb je andere supervised learning methodes overwogen?

&#x20;> Nee, XGBoost komt het vaakst voor in de literatuur en industry practise

\- Waarom doe je grid search in iteratie 2 xgboost als je bijna alleen maar continue waarden hebt?

&#x20;> Goed punt, in princiepe had ik direct kunnen beginnen met bayesian optimization. Uiteindelijk meer gedaan uit nieuwsgierigheid om te zien hoe goed het zou werken.

\- Why stop at 5 iterations on the DQN?

&#x20;> Not enough words in my thesis left to continue iterating, if i had the opportunity i would have started by changing the model architecture

\- Why arent lin et al, zhinin vera and vimal et al mentioned in literature overview?

&#x20;> at that point of the research these papers werent relevant yet. these papers dive deep in the way of implementing RL in a markov decision problem not necessarily interesting to mention as literature on RL in finance

\- Je noemt walk forward validation, maar theoretisch gezien zou je toch ook normale cross validation kunnen gebruiken?

&#x20;> Dit is mogelijk de interesantste vraag. Theoretisch gezien is het mogelijk om cross validation toe te passen. Dit kan door de train folds agregrates mee te geven en de test fold alleen de train set historie zodat er voor elke fold geen data leakage komt. maar het grootste probleem dat je dan creert is het feit dat je dan de volgorde van de dataset aan het veranderen bent voor het creeren van de aggregrates waardoor laundering patterns niet meer kunnen kloppen. Ook zijn de verschillende folds dan niet vergelijkbaar omdat elke fold andere agregrates bevat. Daarom is het toch niet praktisch om cross validation toe te passen maar het is theoretisch gezien wel mogelijk.

\- Figuur 12?

&#x20;> Fout in de legenda

\- Why only 2500 transactions on shap explanation?

&#x20;> Takes a very long time to compute for dqn, 2500 is already on the higher side. lower amounts have been tested and shown that there is little difference

\- Je voegt alleen maar features toe, zijn er features die je beter had kunnen verwijderen?

&#x20;> Ja, er zaten features tussen die niet echt iets toevoegen. Een onnodige feature minder zou niet perse wonderen moeten veroorzaken, maar denk aan de feature sent and receeved currencies, deze komen amper voor of hebben weinig impact in de individuele transacties en global feature importance, dit is 2 categoriën minder voor xgboost, en 26 one hot encoded features minder voor het DQN model. Dit is wel ineens een groot verschil en had meegenomen moeten worden.

\- De SHAP waarden van het XGBoost model zijn in hele andere ranges dan die van de DQN, wat betekent dit?

&#x20;> Het DQN model heeft erg veel moeite met het effectief gebruik maken van features, vandaar dat alle features tegen de nul aanzitten. Het model heeft niet geleerd de features effectief te gebruiken.

\- Hoe kijk je ernaar dat je de features hebt geoptimaliseerd voor XGBoost?

&#x20;> Positief en Negatief. Het positieve is dat mijn onderzoek gaat over hoe goed RL is in tegenstelling tot Supervised learning, daarom is het belangrijk dat beide modellen getest worden in identieke scenarios. Maar het negatieve hiervan is dat je niet het maximale potentie van de DQN opzoekt. Dit had opgelost kunnen worden door een onderzoeks vraag toe te voegen waarin de maximale potentie van de dqn wordt opgezocht, aangezien in mijn onderzoek ik de potentie probeer te maximaliseren met mogelijk sub optimale feature engineering.



**Onnauwkeurige Vragen:**

\- Waarom gebruik je niet de dataset van de competitie?

&#x20;> Dit is een fraud dataset. Niet een AML dataset.

\- Waarom zou je een replay buffer gebruiken? als elke transactie gebasseerd is op oudere transacties dan is dit toch niet logisch aangezien het de chronologie verbreekt?

&#x20;> Fout, tijdens het data pre-processing is de historische data gebruikt om toe te voegen per transactie, vanaf dat punt maakt het niet meer uit hoe er getraint wordt.



**Obscure Vragen:**

\- Wat is het verschil tussen een business rule en een static rule?

&#x20;> Hetzelfde

\- in 1.2.2 vermeld je expliciet dat het onderzoek van Qayoom fraud detection wat verschilt van je eigen onderzoek. Dit zeg je niet over het andere onderzoek dat ook over fraud detection gaat?

&#x20;> Klopt, dit is een schrijf fout. De disclaimer had moeten vermelden dat beide onderzoeken gaan over fraude detectie in plaats van anti-money laundering.



**Vragen Vanuit AI:**

\- Waarom single-step episodes en niet multi-step? (sequentiële transacties van dezelfde account zouden ook als episode gemodelleerd kunnen worden)

&#x20;> literatuur doet dit ook

\- Waarom een replay buffer van de volledige trainingsset? Is dat niet extreem geheugenintensief?

&#x20;> jawel maar de litertuur doet dit ook en ik heb de computational resources om dit aan te kunnen

\- Waarom heb je de DQN architectuur overgenomen van Qayoom et al. terwijl hun trainingsset slechts 248 samples had en die van jou 6.6 miljoen?

&#x20;> Duidelijk de beste vraag en deze zal sowieso komen ook. Ik begon met een klein architectuur aangezien dit in een andere paper gebruikt is. Voordat ik de architectuur ging veranderen wilde ik zeker zijn dat de architectuur ook ingewikkelder moet. Dit heb ik aangetoond door een hoop te experimnetern in de iteraties

\- Waarom gebruik je een discount factor γ als elke episode single-step is? Bij single-step episodes maakt γ niets uit — toekomstige rewards bestaan niet.

&#x20;> **Zoek uit waarom discount factor geen nut heeft**

\- Waarom heb je pair\_tx\_count op 0 gezet voor unseen pairs in de validatie/testset? Is dat een correcte aanname?

&#x20;> Eigenlijk had ik voor de testset de trainset+validatieset aggregrates moeten toevoegen aan de testset. nu mist de testset een chunk aan informatie (15%) omdat de validatie set info compleet mist.

\- Sender\_account en Receiver\_account zitten nog in je feature set — wat voegen die toe bovenop de aggregates die er al van zijn afgeleid?

&#x20;> goed punt, deze zouden verwijderd moeten worden aangezien dit geen betekenisvolle informatie kan leveren

\- Je test AUPRC van XGBoost (0.9275) is hoger dan je validatie AUPRC (0.9136) — normaal verwacht je het omgekeerde. Hoe verklaar je dit?

&#x20;> dit kan ik niet volledig verklaren. Het verschil is erg klein en het kan zijn dat de testset net wat makkelijker is voor het getraind model.

\- Hoe interpreteer je het feit dat DQN Iteration 3 een hogere test AUPRC heeft dan Iteration 2, terwijl Iteration 2 een hogere validatie AUPRC had?

&#x20;> run to run variability

\- SAML-D is gebaseerd op UK banking data — hoe representatief is dit voor Nederlandse banken zoals ING en ABN AMRO?

&#x20;> niet aangezien de UK niet deel is van de EU

\- Je fraud rate in de testset (0.119%) is hoger dan in de trainingsset (0.102%) — kan dit de resultaten beïnvloeden?

&#x20;> het verschil in imbalance rate is zodanig klein dat dit de resultaten niet significant zou moeten beïnvloeden

\- ABN AMRO toont investigators de top 3 features per alert — kun je met jouw DQN hetzelfde doen gezien de near-zero SHAP waarden?

&#x20;> ja maar dit heeft niet veel betekenis

\- Je gebruikt KernelExplainer voor de DQN — hoe betrouwbaar zijn die approximate SHAP waarden vergeleken met de exacte TreeExplainer waarden van XGBoost?

&#x20;> dit kan ik niet met zekerheid zeggen omdat ik de kernelexplainer niet heb gebruikt voor de XGBoost. dit is een gemiste kans voor een eerlijke vergelijking

\- Je conclusie is dat RL niet effectief is voor AML — maar is dit een conclusie over RL in het algemeen, of alleen over DQN op tabular data met deze specifieke setup?

&#x20;> DQN met tabular data met deze specifieke setup

\- Je zegt dat XGBoost near-optimal presteert met default parameters — hoe weet je dat verdere feature engineering niet meer had opgeleverd dan hyperparameter tuning?

&#x20;> baseer ik op het feit dat de features die minder goed gedecteerd worden graph based data vereisen.

