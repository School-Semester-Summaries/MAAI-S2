*Aantekeningen anti-money laundering presentatie. Kees van Montfort presenteert alleen. Michiel Bontebal is niet aanwezig.*

## Introduction Anti Money Laundering
### Wat voor sort frauds kunnen er binnen een bedrijf plaats vinden? 
2016 cijfers, 2410 cases gereport. 69% man, 31% vrouw. Posities zijn 41% werknemer en x% etc (kijk slide)
### Indicaties/Red flags van financiele fraude
living beyond means 45.8%, financiele moeilijkheden 30.0%. Close relationship 20.1% (een goede contact persoon bijv. Ict afedeling). Unwillingness to share duties 15.3%, wheeler-dealere attitude 15.3%, Divorce/family problems13.4%, irritability suspiciousness, defenisiveness 12.3%, addiction problems 10%.
### Fraudeboom
hierin kun je alle vormen van fraude terug vinden. Corruptie, Financial Statement Fraud, Asset misappropriation. Elke vorm heft meerdere subvormen.
### Grote financiele fraudes
Enron heeft er mogelijk voor gezorgd dat Arthur anderson is failliet gegaan. Ahold ook problemen veroorzaakt.
### Deteceteren van witwas praktijken. 
Wet te voorkoming van witwassen financiering en terrorisme (WWFT) hebben de plicht dat er geen witwas geldstromen over bankrekeningen gaan. Wet heeft grote gevolgen, ING kreeg 750 miljoen boete omdat overheid vond dat ing er te weinig aan deed. ABN 500 mil boete omdat zze er te weinig aandeden. Bunbank 45 miljoen boete, aangetoond dat ze het wel deden en kwijt gescholden.
Maar hoe detecteer je dit? Miljarden transacties per jaar bij ABN amro. Binnen deze miljarden wil je verdachte transacties eruit halen. Deze verdachte transacties worden ook wel red flags genoemd. Stel iemand neemt ergens 100.000 euro op. Dan wordt die persoon opgebeld. Als het niet vertrouwt wordt wordt je bankrekening afgesloten. Zonder zwart op wit mag je eruit geschopt worden. Als de bank je vragen stelt die jij niet goed kunt onderbouwen hebben zij de bevoegdheid om je rekening stop te zetten.
Fraudeleuse praktijken zoeken in een dataset is als het zoeken van een speld in een hooiberg.
### Dataset soorten
Unsupervised, dit bevat van alles denk aan: tijd, datum, sender receiver accoutn details. Geldbedrag, payment type(credit, debit, cash etc.), sender receiver bank location, currency.
Supervised, deze dataset heft al een een waarde “is_suspicious” die aantoont of een transactie fraudeleus is.
Transactie toelichtingen mogen niet worden ingezien door banken wel door de belastingdienst.
### Red Flags
-	Mogelijkheden dat er iets stinkt. Rond bedrag. Denk aan $5.000, $10.000.
-	Naar welke land je geld overmaakt, Iran, Rusland 
-	Smurfing -> 10 keer $1000 euro overmaken.
-	Nesting -> Geld overmaken door middel van een middleman. Geen rechtstreekse betaling, maar via een tussenpersoon.
-	Shell Company characteristics > ... onduidelijk
-	Non adherence to Fatf recommendations
-	Structuring
-	Cash_withdrawal
-	Deposit-send
-	.... veel meer in de slides
### Basic AI Methods
Verschillende manieren om fraudeleuze transacties te detecteren. Unsupervised kun je gebruiken. Ook kun je supervised gebruiken hierbij zijn submethoden zoals: XGBoost Logistic regressions, random forest, decision tress, knn, ann.
### Performance Measures of algorithms
Hoe kun je een indicatie geven of je AI model goed werkt. Vijf mogelijke indicatoren die je kunt gebruiken, Accuracy, Precision, Recall, F1, F2, F3, F4. Belangrijk om deze te begrijpen en te overwegen welke het meest relevant is voor fraudedetectie. Sem kaart Area under curve precision recall.

### Communicatie
Kees reageert snel via Teams
