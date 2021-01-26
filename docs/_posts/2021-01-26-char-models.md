---
title: On character-level models
---
We attempt to classify the data using character-level (rather than word-level) models

Give out past experiences with the Bag-of-words plus Logistic regression model [^colab7], and the relatively small amount of data, we expect that the character-level models will underperform word-level models.

### N-gram + TF-IDF + Logistic regression model
In this model [^colab10], we generate n-grams of 2 to 4 characters, calcuated the TF-IDF weight of each n-gram and then pass the result weight matrix to Logistic regression. This model has no notion of words or sequences. Even so, the model achieves an accuracy score of 97.28%, F1 score 75.42% and Area-under-curve (AUC) score of 96.40%. 

### Char CNN model
Next we try a character-level CNN model based on [^paper1]. The model in [^colab11] is not as deep as the one described in the paper. We chose a shallower model to keep training times small. Also, we recognize that there wasn't enough data to train a deeper model. The model achieves an accuracy score of 97.39%, F1 score 70.83% and Area-under-curve (AUC) score of 94.48%.

### Applicability to other data sets
While the performance of the character-level models is not as good as some of the other models discussed in this project, the performance exceeds our expectations. They hold promise for classifying larger datasets with cryptic (e.g., slang and code words) or corrupted (e.g., excessive spelling mistakes) communication.

### References
[^colab7]: [Logistic regression plus bag-of-words model](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
[^colab10]: [N-gram + TF-IDF + Logistic regression model](https://github.com/r-dube/fakejobs/blob/main/fj_ngram_tfidf_logistic.ipynb)
[^colab11]: [Char CNN model](https://github.com/r-dube/fakejobs/blob/main/fj_char_cnn.ipynb)
[^paper1]: [Character-level Convolutional Networks for Text Classification](https://arxiv.org/pdf/1509.01626.pdf)
