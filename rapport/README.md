### Content
- [Master_Thesis_KG_v0.1.pdf](./Master_Thesis_KG_v0.1.pdf) ~ 70% Versie
- [Master_Thesis_KG_v0.2.pdf](./Master_Thesis_KG_v0_2.pdf) ~ 70% Versie maar ik heb mezelf feedback gegeven en toegepast op H1: (Mijn eigen feedback document - [Zelf Feedback geven op Thesis H1](../𝒲𝐼𝒦𝐼✨/Feedback%20en%20Iteratie/Thesis/Master_Thesis_KG_v0.1%20-%20Feedback%20H1%20-%20Kaan%20Gogcay.pdf))
- [Master_Thesis_KG_v1.9.pdf](./Master_Thesis_KG_v1.9.pdf) ~ 100% Versie: 

### Rapportstructuur
100% Versie Rapportstructuur en waar de content van het rapport uit is ontstaan. Dit kan betekenen dat de content is geëvalueerd in de text die je ziet in de thesis, maar het kan ook betekenen dat de content 1 op 1 is gekopieërd naar de thesis. Als de text uit de thesis niet is ontstaan uit bestaande content is het direct in de thesis geschreven. Eerdere versies van het rapport en het pva zijn buiten beschouwing gelaten omdat alles is geËvalueerd uit eerdere versies van het rapport en pva.

1 Introduction
- 1.1 Context Analysis ~ ([Context_v1.md](../𝒲𝐼𝒦𝐼✨/Onderzoek/old_conceptual_research/Context_v1.md))
    - 1.1.1 Money Laundering ~ ([Context_v1.md](../𝒲𝐼𝒦𝐼✨/Onderzoek/old_conceptual_research/Context_v1.md))
    - 1.1.2 Money Laundering Detection ~ ([Context_v1.md](../𝒲𝐼𝒦𝐼✨/Onderzoek/old_conceptual_research/Context_v1.md))
    - 1.1.3 Traditional AML Methods and its Limitations ~ ([Context_v1.md](../𝒲𝐼𝒦𝐼✨/Onderzoek/old_conceptual_research/Context_v1.md))
- 1.2 Literature Overview
    - 1.2.1 State of the Art
    - 1.2.2 Reinforcement Learning, an Emerging Method
- 1.3 Industry Insights
    - 1.3.1 ING ~ ([ING](../𝒲𝐼𝒦𝐼✨/Onderzoek/ING/))
    - 1.3.2 ABN AMRO ~ ([ABN AMRO](../𝒲𝐼𝒦𝐼✨/Onderzoek/ABN%20AMRO/))
    - 1.3.3 DLL ~ ([DLL](../𝒲𝐼𝒦𝐼✨/Onderzoek/DLL/))
- 1.4 Identified Gap
- 1.5 Scope
- 1.6 Research Question ~ ([Hoofdvraag_en_Deelvragen_v2.md](../𝒲𝐼𝒦𝐼✨/Onderzoek/old_conceptual_research/Hoofdvraag_en_Deelvragen_v2.md))
2 Background
- 2.1 Relevant Literature on Techniques
    - 2.1.1 Reinforcement Learning and Deep Q-Networks
    - 2.1.2 Explainability with SHAP
- 2.2 Related Work Comparison
- 2.3 AI Suitability Justification
- 2.4 Ethical and Societal Considerations
    - 2.4.1 False Positives and Customer Impact
    - 2.4.2 Bias and Fairness
    - 2.4.3 Labeling Bias
    - 2.4.4 Explainability as an Ethical Requirement
    - 2.4.5 Data Privacy
3 Methodology
- 3.1 Research Overview
- 3.2 Requirements
- 3.3 Data
    - 3.3.1 Dataset Selection ~ ([Dataset_v1.md](../𝒲𝐼𝒦𝐼✨/Onderzoek/old_conceptual_research/Dataset_v1.md))
    - 3.3.2 Data Split ~ ([Data Exploration and Preperation Notebook](../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb))
    - 3.3.3 Feature Engineering ~ ([Data Exploration and Preperation Notebook](../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb))
- 3.4 Evaluation Metric
- 3.5 Models
    - 3.5.1 Baseline Definition: XGBoost
    - 3.5.2 XGBoost Iterations ~ ([XGBoost Notebook](../code/XGBoost/XGBoost_v9.1.ipynb))
    - 3.5.3 Reinforcement Learning: Deep Q-Network ~ ([DQN Notebook](../code/DQN/DQN_v7.2.ipynb))
- 3.6 Prototype & AI Design Patterns & Stakeholder Evaluation
    - 3.6.1 Prototype
    - 3.6.2 AI Design Patterns
    - 3.6.3 Stakeholder Evaluation ~ ([Stakeholder Evaluation](../𝒲𝐼𝒦𝐼✨/Onderzoek/Prototype%20Testen/))
    - 3.6.4 Level of Automation
4 Results
- 4.1 Performance ~ ([Comparison Notebook](../code/Comparison/Comparison%20Notebook_v0.1.ipynb))
- 4.2 Explainability
    - 4.2.1 Global Feature Importance ~ ([Comparison Notebook](../code/Comparison/Comparison%20Notebook_v0.1.ipynb))
    - 4.2.2 Individual Transaction Analysis ~ ([Comparison Notebook](../code/Comparison/Comparison%20Notebook_v0.1.ipynb))
- 4.3 Robustness ~ ([Comparison Notebook](../code/Comparison/Comparison%20Notebook_v0.1.ipynb))
- 4.4 Model Complexity
- 4.5 Resource Demand
5 Discussion
- 5.1 Evaluation of Results
- 5.2 Evaluation of Design Choices and Iterations
- 5.3 Limitations
- 5.4 Reliability, Validity and Generalisability
- 5.5 Ethical and Societal Reflection
6 Conclusion
References
Appendices
- A Requirements
    - A.1 Legal & Ethical Requirements
    - A.2 Functional Requirements
    - A.3 Technical Requirements
- B SAML-D Feature Overview ~ ([Data Exploration and Preperation Notebook](../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb))
- C Laundering Type Descriptions ~ ([Data Exploration and Preperation Notebook](../code/EDA/Data_Exploration_and_Preperation_v1.7.4.ipynb))
- D Feature Engineering Iterations 
    - D.1 Feature Engineering — Iteration 1: Raw Features ~ ([Data Exploration and Preperation Notebook](../code/EDA/
    - D.2 Feature Engineering — Iteration 2: Account-level Aggregates ~ ([Data Exploration and Preperation Notebook](../code/EDA/
    - D.3 Feature Engineering — Iteration 3: Pair History ~ ([Data Exploration and Preperation Notebook](../code/EDA/
    - D.4 Engineered Feature Overview ~ ([Data Exploration and Preperation Notebook](../code/EDA/
- E XGBoost Iteration Details ~ ([XGBoost Notebook](../code/XGBoost/XGBoost_v9.1.ipynb))
- F Stakeholder Evaluation Details ~ ([Stakeholder Evaluation](../𝒲𝐼𝒦𝐼✨/Onderzoek/Prototype%20Testen/))