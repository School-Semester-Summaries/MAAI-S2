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

> ⚠️ **Observatie:** De gebruiker herinnerde zich niet dat de data synthetisch is. Het synthetische karakter van de data is onvoldoende blijven hangen.

---

### 1b. Explainability
| Vraag | Antwoord |
|---|---|
| Was de weergegeven informatie duidelijk en begrijpelijk? | Ja, maar technische achtergrond vereist. `fan_out_ratio` was onduidelijk — een percentage zou beter lezen |
| Kon je het volledige overzicht vinden? | Ja |
| Is er iets wat niet duidelijk is in het overzicht? | Accounttype ontbreekt — zakelijk vs. privé is relevant voor de beoordeling |

> **Observaties:**
> - Gebruiker had initieel moeite een transactie in detail te openen, maar loste dit zelf op
> - Gebruiker wil de transactiegeschiedenis van sender en receiver kunnen bekijken voor context — het model heeft deze context wel maar de gebruiker niet
> - Gebruiker kon niet vaststellen of `****5678` in twee transacties hetzelfde account betreft
> - Gebruiker kende de meeste patronen al, maar suggereerde uitleg van patronen toe te voegen aan de tool
> - Gebruiker begreep dat `Normal_*` patronen normale transacties zijn en geen witwassen

---

## Taak 2 — Threshold instellen
*Open het configuratie menu en breng de threshold naar een waarde zodat de aantal transacties vandaag beoordeelbaar is door het team.*

### 2a. Feedback en Control
| Vraag | Antwoord |
|---|---|
| Hoe ben je tot deze threshold gekomen? | Berekend: 5 analisten × 16 transacties/dag (bij 30 min per transactie, 8 uur werktijd) = 80 transacties per dag |
| Wat is er op je scherm veranderd? | Het aantal getoonde transacties |
| Begrijp je alle vertoonde statistieken? | Ja, maar de statistieken (recall, precision, FP per TP) verraden informatie die je in werkelijkheid niet zou mogen weten |

> ⚠️ **Observatie:** Prototype vertoonde een fout bij het spelen met de threshold.

---

## Taak 3 — Foutafhandeling testen
*Probeer de transacties zo te filteren met de sliders dat er 0 transacties geflagged worden. Zorg er daarna voor dat er weer transacties geflagged worden.*

### 3a. Error Handling
| Vraag | Antwoord |
|---|---|
| Is het duidelijk waarom er geen transacties zijn geflagged? | Ja — niets heeft een hogere confidence score dan 100% |
| Is het duidelijk hoe je dit probleem oplost? | Ja — slider terugsliden |
| Heeft het foutbericht geholpen? | Bericht niet gelezen, want het was al zichtbaar dat er 0 transacties waren |

> **Observaties:**
> - Gebruiker vond het vreemd dat de threshold een ruwe score is terwijl de confidence als percentage wordt weergegeven — dit creëert inconsistentie
> - Na enig gebruik werd de relatie tussen threshold en confidence duidelijk, maar de initiële onbekendheid was een drempel

---

## Taak 4 — Modellen vergelijken en rapporteren
*Open een flagged transaction en vergelijk hoe beide modellen de transactie scoren. Report deze case en maak een schatting wat het patroon is.*

### 4a. Safety
| Vraag | Antwoord |
|---|---|
| Viel je iets op toen je switchte van model? | Kon de modeloptie initieel niet vinden (hulp nodig). Na het switchen was een andere transactie geselecteerd. De waarschuwing viel op maar werd niet gelezen. DQN bevat erg veel ruis |
| Heeft het waarschuwingsbericht veranderd hoe je omgaat met DQN-beoordelingen? | N.v.t. — bericht niet gelezen |

### 4b. Privacy
| Vraag | Antwoord |
|---|---|
| Hoe kijk je ernaar dat account-IDs niet volledig zijn weergegeven? | Positief, maar jammer — je kunt niet zien of dezelfde accounts terugkomen over meerdere transacties. Intern zou volledige weergave geen probleem moeten zijn |

> **Observaties:**
> - DQN toont bijdrages van locaties die niet relevant zijn voor de transactie (bijv. andere bank locations terwijl de transactie volledig UK is), wat verwarrend is
> - Gebruiker wil zien op basis van welke andere transacties een verdict is gebaseerd (bijv. bij Fan\_In alle bijbehorende transacties zien)

---

## Overige Feedback

| Onderwerp | Feedback |
|---|---|
| Lage percentages in uitleg | Bijna alle variabelen zijn interessant, ook lage bijdrages. Account-IDs hoeven niet in de verklaring te staan — die staan al in de tabel |
| Standaardverdeling | Gebruiker wil niet alleen de afwijking zien maar ook de onderliggende verdeling en alle waarden daarin |
| Groene kolom (decreases suspicion) | Te veel items — scrollen wordt te veel. Mogelijke oplossing: drempelwaarde voor minimale bijdrage |

---

## Samenvatting Bevindingen

| Design Pattern | Bevinding | Actie |
|---|---|---|
| Transparency | Synthetische aard van data niet onthouden | Disclaimer prominenter maken of herhalen in de interface |
| Explainability | Technische variabelenamen en ontbrekende context (accounttype, geschiedenis) | Tooltips toevoegen, variabelenamen verder versimpelen |
| Feedback & Control | Threshold inconsistent met confidence percentage | Threshold omzetten naar percentage (0–100%) |
| Error Handling | Foutbericht niet gelezen maar situatie wel begrepen | Foutbericht is voldoende; geen aanpassing nodig |
| Safety | DQN-waarschuwing niet gelezen; modelswitch reset geselecteerde transactie | Waarschuwing visueel prominenter maken |
| Privacy | Gemaskerde IDs belemmeren vergelijking van accounts | Overweeg optie voor intern gebruik zonder masking |
