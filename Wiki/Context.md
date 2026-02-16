# Context <!-- (“What does the reader need to understand before the problem makes sense?”) -->
## Money Laundering <!-- (What is money laundering?) -->
Money laundering is the process of concealing the illegal origin of funds to make them appear legitimate, allowing criminals to use the proceeds in the legal economy (FIU-the Netherlands, 2023) (Financial Crimes Enforcement Network, n.d.). These funds often come from crimes such as drug trafficking, fraud, or illegal pornography, tax evasion, robbery, blackmail, bribery, piracy and people trafficking (Cox, 2012) (FIU-the Netherlands, 2023). Once obtained, the money cannot be spent freely, so criminals must disguise its illegal origin. This is achieved through the money-laundering process, which typically occurs in three stages: placement, layering and integration (Cox, 2012). 
<this link is from different pages, another citation? Or update the pages?>
<Consider flow Image here of the proces>

### Placement
Placement is the first step in the laundering process. In this step, criminals attempt to introduce their funds into the financial system. This is often associated with depositing cash into bank accounts, but placement is not limited to plain deposits. Some examples of introducing criminal money to the financial system cover: purchasing artwork, antiques and lottery tickets.

### Layering
Once criminally earned funds have been introduced to the financial system, criminals try to hide the origin of this money. This can be done in various ways, such as investing in legitimate assets, buying and selling collectibles, or making multiple smaller transactions across different accounts. The more these funds are moved back and forth, the harder it becomes to trace their original source.

### Integration
Once the origin of illegal funds is difficult to trace, criminals can freely integrate their laundered money into the economy. This can be done by investing in businesses, purchasing property, buying jewellery, or other assets that appear legitimate.

## Money Laundering Detection <!-- (What is money laundering detection?) -->
Money laundering detection or AML (anti-money laundering) refers to the process of detecting money laundering. AML technology has changed significantly over the past years. Evolving from dedicated AML teams to semi-automized machine learning workflows (Weber, 2018).

## Limitations of Traditional AML Methods <!-- (What are the limitations of traditional methods?) -->
Initially, companies relied on dedicated AML (Anti-Money Laundering) departments where employees were trained to manually identify suspicious transactions. With the growth of transaction volumes, rule-based systems became one of the first forms of automated detection. These systems typically monitored transactions and generated alerts for activity exceeding thresholds, such as amounts over $10,000, amounts just below $10,000, or multiple smaller transactions within 24 hours that collectively surpassed $10,000. While rule-based systems improved efficiency, they had limitations in handling complex laundering patterns and large-scale data, which led to the adoption of more advanced methods, including graph analytics, machine learning, and deep learning techniques.

## Machine Learning in AML <!-- (Why even use machine learning? Which techniques have been used in AML? Why could Reinforcement Learning be interesting to research?) -->
Machine learning is often proposed as an alternative to traditional rule-based AML systems because of its ability to model complex patterns. Rule-based approaches rely on manually defined rules and fixed thresholds, which makes them less flexible and more likely to produce many false positives and struggle when patterns change over time. In contrast, machine learning models can learn complex relationships from data and adapt to new laundering strategies over time. This dynamic nature makes machine learning particularly suitable for detecting sophisticated and previously unseen laundering techniques that would not be captured by predefined rules.

Prior literature shows that a wide range of machine learning approaches have been applied to AML. Most studies rely on supervised learning (Nazanin Bakhshinejad, 2022). However, due to the scarcity and noisiness of labelled AML data, unsupervised and semi-supervised methods have also received attention.

Little research has been conducted on reinforcement learning in AML. Typically, reinforcement learning requires an environment that an agent can interact with, which is not naturally present in AML settings. Instead, AML research mostly relies on synthetic datasets rather than interactive environments. However, with creative engineering, it is possible to simulate an environment that allows an agent to interact with the data, making reinforcement learning a potentially interesting direction for further research.

Bibliography
###### 1. Cox, D. (2012). Handbook of Anti-Money Laundering. In D. Cox, Handbook of Anti-Money Laundering (pp. 5-13). John Wiley & Sons.
###### 2. Financial Crimes Enforcement Network. (n.d.). What is money laundering? Retrieved from FinCEN.gov: https://www.fincen.gov/what-money-laundering
###### 3. FIU-the Netherlands. (2023). What is money laundering? Retrieved from FIU-Nederland: https://www.fiu-nederland.nl/en/home/what-is-money-laundering/
###### 4. Nazanin Bakhshinejad, R. S. (2022). A Survey of Machine Learning Based Anti-Money Laundering. 
###### 5. Weber, M. (2018). Scalable Graph Learning for Anti-Money Laundering: A First Look. 


