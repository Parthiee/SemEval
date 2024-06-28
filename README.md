
# Emotion Classification in Hindi-English Code-Mixed Dialogue using Transformer-based Models

This repository contains the data and programs associated with the 10th task of SemEval 2024. The task is to classify Hinglish dialogues based on emotions, into eight different classes.

The preprocessing files contain code for text normalization, Levenshtein distance calculation, removal of names and stopwords.

There are seven notebooks, each of which with a different type of model.

We observe that HingRoberta performs the best with a weighted-F1 score of 0.45. We placed 7th out of 38 submissions for this task. 






## Paper

The paper describing the method used for this task can be found here: 


[Emotion Classification in Hindi-English Code-Mixed Dialogue using Transformer-based Models](https://aclanthology.org/2024.semeval-1.119/)
## Methodology


We utilize three kinds of models- simple machine learning models, RNN-based LSTM/Bi-LSTM models, as well as Transformer Models for Hindi and Hindi-English code mixed data. 

### Architecture

![image](https://github.com/pooja-premnath/SemEval2024-Emotion-Classification-in-Hinglish-Code-Mixed-Dialogue-using-Transformer-based-Models/assets/88699435/e32abd8e-765e-4028-a9e6-06385c419b36)


The precision scores and performance metrics of each are as follows: 

### Machine Learning Models

| **Emotion**  | **SVM**  | **MNB**  | **RF**   |
|--------------|----------|----------|----------|
| **Anger**    | 0        | 0.12     | **0.19** |
| **Contempt** | **0.33** | 0        | 0.17     |
| **Disgust**  | 0        | 0        | **1**    |
| **Fear**     | **0.33** | 0        | 0.24     |
| **Joy**      | 0.55     | **0.58** | 0.55     |
| **Neutral**  | 0.43     | 0.43     | **0.44** |
| **Sadness**  | 0        | 0.27     | **0.28** |
| **Surprise** | 0.22     | **0.29** | 0.27     |




| **Metric**              | **SVM**  | **MNB** | **RF**   |
|-------------------------|----------|---------|----------|
| **Testing Accuracy**    | **0.44** | 0.4     | 0.43     |
| **Testing Weighted F1** | 0.31     | 0.3     | **0.33** |



### RNN- based Models

| **Emotion**  | **Bi-LSTM Precision Values** |
|--------------|------------------------------|
| **Anger**    | 0.06                         |
| **Contempt** | 0.08                         |
| **Disgust**  | 0.017                        |
| **Fear**     | **0.48**                     |
| **Joy**      | 0.38                         |
| **Neutral**  | 0.12                         |
| **Sadness**  | 0.12                         |
| **Surprise** | 0.21                         |

| **Metric**              | **Bi-LSTM Model** |
|-------------------------|-------------------|
| **Testing Accuracy**    | 0.35              |
| **Testing Weighted F1** | 0.43              |


### Transformer Models

| **Emotion**  | **HingBERT** | **Hing mBERT** | **Hing RoBERTa** |
|--------------|--------------|----------------|------------------|
| **Anger**    | 0.28         | 0.27           | **0.33**         |
| **Contempt** | 0.19         | 0.16           | **0.26**         |
| **Disgust**  | **0.25**     | 0.2            | 0.2              |
| **Fear**     | 0.24         | 0.23           | **0.34**         |
| **Joy**      | 0.45         | 0.49           | **0.54**         |
| **Neutral**  | **0.52**     | **0.52**       | **0.52**         |
| **Sadness**  | 0.35         | 0.28           | **0.36**         |
| **Surprise** | 0.31         | **0.34**       | 0.3              |


| **Metric**              | **HingBERT** | **Hing mBERT** | **Hing RoBERTa** |
|-------------------------|--------------|----------------|------------------|
| **Testing Accuracy**    | 0.45         | 0.44           | **0.47**         |
| **Testing Weighted F1** | 0.42         | 0.43           | **0.45**         |

## Authors


- [Pooja Premnath](https://github.com/pooja-premnath)
- [Y.V. Ojus](https://github.com/Ojus999)
- [Parthiban M.](https://github.com/Parthiee)
## Citation

If you find our work helpful, please consider including the following citation:


```
@inproceedings{yenumulapalli-etal-2024-techssn1,
    title = "{TECHSSN}1 at {S}em{E}val-2024 Task 10: Emotion Classification in {H}indi-{E}nglish Code-Mixed Dialogue using Transformer-based Models",
    author = "Yenumulapalli, Venkatasai Ojus  and
      Premnath, Pooja  and
      Mohankumar, Parthiban  and
      Sivanaiah, Rajalakshmi  and
      Deborah, Angel",
    editor = {Ojha, Atul Kr.  and
      Do{\u{g}}ru{\"o}z, A. Seza  and
      Tayyar Madabushi, Harish  and
      Da San Martino, Giovanni  and
      Rosenthal, Sara  and
      Ros{\'a}, Aiala},
    booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.semeval-1.119",
    pages = "833--838",
    abstract = "The increase in the popularity of code mixed languages has resulted in the need to engineer language models for the same . Unlike pure languages, code-mixed languages lack clear grammatical structures, leading to ambiguous sentence constructions. This ambiguity presents significant challenges for natural language processing tasks, including syntactic parsing, word sense disambiguation, and language identification. This paper focuses on emotion recognition of conversations in Hinglish, a mix of Hindi and English, as part of Task 10 of SemEval 2024. The proposed approach explores the usage of standard machine learning models like SVM, MNB and RF, and also BERT-based models for Hindi-English code-mixed data- namely, HingBERT, Hing mBERT and HingRoBERTa for subtask A.",
}

```
