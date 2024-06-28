
# Emotion Classification in Hindi-English Code-Mixed Dialogue using Transformer-based Models

This repository contains the data and programs associated with the 10th task of SemEval 2024. The task is to classify Hinglish dialogues based on emotions, into eight different classes.

The preprocessing files contain code for text normalization, Levenshtein distance calculation, removal of names and stopwords.

There are seven notebooks, each of which with a different type of model.

We observe that HingRoberta performs the best with a weighted-F1 score of 0.45. We placed 7th out of 38 submissions for this task. 






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
