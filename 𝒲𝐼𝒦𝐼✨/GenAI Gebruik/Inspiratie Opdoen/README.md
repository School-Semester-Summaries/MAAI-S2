Prompt
```md
i will visit DLL tomorrow! 🥳

HOWEVER I HAVE NO IDEA WHY I AM GOING WHAT SHOULD I ASK????

these are some ideas:

DLL is a lease company, do you get in contact with Money Laundering at all?
are you able to give numbers?
what techniques do you use?
how well do the models perform?
are there models you wanted to try but werent able to try?
basically all things that i also asked abn amro and rabobank?

but also very important in this interview, i have to see interfaces, products, i need inspiration for my own prototype,
```

Answer
```md
Congrats! Here's a structured set of questions organized by goal:

**Grounding questions (context)**
- Does DLL encounter money laundering directly as a lease company, or is it more adjacent (e.g. through financing arrangements)?
- Are you subject to the Wwft, and how does that shape your AML approach?
- Roughly what volume of transactions do you monitor?

**Technical questions (stakeholder insight)**
- What models or techniques do you currently use for AML detection?
- How do you handle class imbalance in your transaction data?
- What evaluation metrics do you use — do you use AUPRC or something else?
- Are there models or approaches you wanted to try but couldn't, and why?
- How do you generate labels — rule-based, human investigators, or something else?

**Explainability and prototype inspiration (most important for you)**
- When a transaction is flagged, how do investigators currently review it?
- What information do investigators need to make a decision on a flagged transaction?
- How is explainability currently presented — feature lists, visualizations, scores?
- Can I see the interface investigators use? Even a screenshot or walkthrough would help enormously.
- What would make a flagged transaction explanation immediately clear to a non-technical investigator?
- Is a threshold slider something that would be useful in practice, or is the threshold fixed?

**Feedback on your research**
- Present your AUPRC results briefly and ask: does 0.7739 seem meaningful in a real AML context?
- Show one of your SHAP waterfall plots and ask: would this explanation be useful to an investigator?
- Ask whether the laundering pattern breakdown (smurfing, fan-out etc.) would be useful in their workflow

The prototype inspiration questions are the most important ones. Try to get them to show you something visual — even a rough sketch of their current alert interface will give you ideas for your dashboard.
```