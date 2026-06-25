# Stakeholder Evaluation — AML Transaction Monitor Prototype

**Evaluator:** Financial domain expert  
**Date:** June 2026  
**Duration:** ~35 minutes  
**Format:** Think-aloud protocol with structured questions per task

---

## Taak 1 — Transactie beoordelen en rapporteren
*Open een flagged transaction en probeer zo goed mogelijk te begrijpen waarom deze precies geflagged is. Report dan deze case en maak een schatting welke laundering patroon het zou kunnen zijn.*

### 1a. Transparency
| Vraag | Antwoord |
|---|---|
| Heb je een disclaimer gezien? | Ja |
| Wat is je bijgebleven van de disclaimer? | Testfase voor een project |
| Zou je daar iets aan veranderen? | Nee |

> ⚠️ **Observatie:** De gebruiker gaf aan dat het niet is blijven hangen dat de data synthetisch is.

---

### 1b. Explainability
| Vraag | Antwoord |
|---|---|
| Was de weergegeven informatie duidelijk en begrijpelijk? | Ja, maar ik heb toevallig een technische achtergrond. Dat terzijde, variabelen zoals `fan_out_ratio` zijn alsnog onduidelijk, een percentage zou dit beter maken |
| Kon je het volledige overzicht vinden? | Ja |
| Is er iets wat niet duidelijk is in het overzicht? | Accounttype ontbreekt. zakelijk vs. privé is relevant voor de beoordeling |

> **Observaties:**
> - Gebruiker had initieel moeite een transactie in detail te openen, maar loste dit zelf op
> - Gebruiker wil de transactiegeschiedenis van sender en receiver kunnen bekijken voor context. Deze context zit verspreid over de train, val en test data. Train data is niet beschikbaar in de tool, maar wel op getraind. Val data is compleet absent. Test data bevat wel deze context maar het is niet gebruikersvriendelijk om dezelfde transacties terug te vinden in de tool.
> - Gebruiker kon niet zeker weten of dat als de laatste 4 nummers van een ID overeenkomen, of dit dan daadwerkelijk ook dezelfde user is.
> - Gebruiker kende de meeste patronen al, maar niet allemaal. Dit kan aangepakt worden door uitleg toe te voegen per laundering pattern.
> - Gebruiker begreep dat `Normal_*` patronen normale transacties zijn en geen witwas patronen.

---

## Taak 2 — Threshold instellen
*Open het configuratie menu en breng de threshold naar een waarde zodat de aantal transacties vandaag beoordeelbaar is door het team.*

### 2a. Feedback en Control
| Vraag | Antwoord |
|---|---|
| Hoe ben je tot deze threshold gekomen? | Berekend: 5 analisten × 16 transacties/dag (bij 30 min per transactie, 8 uur werktijd) = 80 transacties per dag |
| Wat is er op je scherm veranderd? | Het aantal getoonde transacties |
| Begrijp je alle vertoonde statistieken? | Ja, maar de statistieken (recall, precision, FP per TP) verraden informatie die je in werkelijkheid niet zou kunnen weten |

> ⚠️ **Observatie:** Prototype vertoonde een error bij het spelen met de threshold.

---

## Taak 3 — Foutafhandeling testen
*Probeer de transacties zo te filteren met de sliders dat er 0 transacties geflagged worden. Zorg er daarna voor dat er weer transacties geflagged worden.*

### 3a. Error Handling
| Vraag | Antwoord |
|---|---|
| Is het duidelijk waarom er geen transacties zijn geflagged? | Ja, niets heeft een hogere confidence score dan 100% |
| Is het duidelijk hoe je dit probleem oplost? | Ja, slide naar een kan heb je alle transacties naar de andere kant heb je niets. |
| Heeft het foutbericht geholpen? | Bericht niet gelezen, want het was al zichtbaar dat er 0 transacties waren |

> **Observaties:**
> - Gebruiker vond het vreemd dat de threshold een ruwe score is terwijl de confidence als percentage wordt weergegeven
> - Na enig gebruik van de thresholds werd de relatie tussen threshold en confidence duidelijk, maar de initiële onbekendheid was een drempel

---

## Taak 4 — Modellen vergelijken en rapporteren
*Open een flagged transaction en vergelijk hoe beide modellen de transactie scoren. Report deze case en maak een schatting wat het patroon is.*

### 4a. Safety
| Vraag | Antwoord |
|---|---|
| Viel je iets op toen je switchte van model? | Kon de modeloptie initieel niet vinden (hulp nodig). Na het switchen van model werd ineens een andere transactie getoond. DQN bevat erg veel ruis. De waarschuwing viel op maar werd niet gelezen. |
| Heeft het waarschuwingsbericht veranderd hoe je omgaat met DQN-beoordelingen? | N.v.t. — bericht niet gelezen |

### 4b. Privacy
| Vraag | Antwoord |
|---|---|
| Hoe kijk je ernaar dat account-IDs niet volledig zijn weergegeven? | Positief, maar jammer. Je kunt niet zien of dezelfde accounts terugkomen over meerdere transacties. Intern zou volledige weergave geen probleem moeten zijn. |

> **Observaties:**
> - DQN toont bijdrages van locaties die niet relevant zijn voor de transactie (bijv. andere bank locations terwijl de transactie volledig UK is), wat verwarrend is
> - Gebruiker wil zien op basis van welke andere transacties een flag is gebaseerd (bijv. bij Fan\_In alle bijbehorende transacties zien)

---

## Overige Feedback

| Onderwerp | Feedback |
|---|---|
| Vind je de lage percentages interesant? zou het erg zijn als deze niet getoond worden? | Bijna alle variabelen zijn interessant, ook lage bijdrages. Account-IDs hoeven niet in de verklaring te staan — die staan al in de tabel |
| Standaardverdeling | Gebruiker wil niet alleen de afwijking zien maar ook de onderliggende verdeling en alle waarden daarin |
| Groene kolom (decreases suspicion) | Te veel items, te veel scrollen voelt een beetje chaotisch. |

---

## Samenvatting Bevindingen

| Design Pattern | Bevinding | Actie |
|---|---|---|
| Transparency | Synthetische aard van data niet onthouden | Disclaimer prominenter maken |
| Explainability | Technische variabelenamen en ontbrekende context (accounttype, geschiedenis) | alle scores (0.0 - 1.0) omzetten in percentages. Accounttype is niet beschikbaar, geschiedenis is out of scope voor dit project, maar wel is het mogelijk om de transacties te laten zien van dezelfde sender/receiver als vergelijkingsmateriaal |
| Feedback & Control | Threshold inconsistent met confidence percentage | Threshold omzetten naar percentage (0–100%). De statistieken: precision, recall en FP per TP zijn interesant en leveren een bijdrage dus mogen zeker in de tool blijven. Maar misschien een optie om ze te verstoppen zodat je de tool realistischer kunt maken. |
| Error Handling | Foutbericht niet gelezen maar situatie wel begrepen | Foutbericht is voldoende; geen aanpassing nodig. Als van model geswitcht wordt tijdens het reviewen van een transactie wordt ineens een andere transactie vertoond. (Ook ontstond er een error tijdens het spelen met de threshold) Deze errors moeten opgelost worden |
| Safety | DQN-waarschuwing niet gelezen | Waarschuwing prominenter maken |
| Privacy | Gemaskerde IDs belemmeren vergelijking van accounts | Overweeg optie zonder masking |
