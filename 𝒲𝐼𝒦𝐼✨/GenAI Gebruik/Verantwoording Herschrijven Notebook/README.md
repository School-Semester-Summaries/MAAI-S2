Uit mijn DQN Notebook:

Prompt
```markdown
how is this
```However, one-hot-encoding the input data is not sufficient to ... . The data consists of data scales which differ drastically. For example, `Amount` ranges from 3.73 to 12618498.40 but `pair_tx_count` ranges from 1 to 62 and all the categorical features are between 0 and 1. inputting this raw will result in the higher numbers having more inpact on the neural networks, which is a known drawback of neural networks. But there are 2 well-known solutions to this problem. Normalization and Standarization.```
```

Answer
```markdown
The reasoning is correct but the writing needs work. A few issues:

- "is not sufficient to ..." — sentence is unfinished
- "data scales which differ drastically" — awkward phrasing
- "inputting this raw" — too informal
- Repetition of "data"
- Typo: "inpact", "Standarization"
- Capitalising Normalization and Standardisation mid-sentence is inconsistent

Here's a rewrite:

---

*One-hot encoding alone does not address the large differences in feature scale across the dataset. For example, `Amount` ranges from 3.73 to 12,618,498.40, while `pair_tx_count` ranges from 1 to 62, and all one-hot encoded features are bounded between 0 and 1. Feeding these raw values into a neural network is problematic because features with larger magnitudes will dominate the gradient updates — a well-known sensitivity of neural networks to input scale (LeCun et al., 1998). Two standard solutions exist: normalisation and standardisation.*

---

Then you go into why you picked standardisation over normalisation, which you already have good reasoning for from our previous messages.
```