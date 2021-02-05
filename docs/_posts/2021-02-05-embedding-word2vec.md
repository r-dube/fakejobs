---
title: Word2Vec experiments to match the performance of Logistic Regression
---
Since Word2Vec performed better than FastText, we experiment with hyper-parameters used to generate the embeddings.

First, we expand the unlabeled data available by obtaining and process another jobs dataset from Kaggle ([^kaggle2]).

Second, we change from the continuous bag-of-words that is the default in Word2vec to Skipgrams.

Finally, we expand the window size used by Gensim to create embedding from the default 5 to 10. The bigger window allows the Word2Vec algorithm to look at more neighboring words while generating embeddings ([^colab14]).

The above changes ([^colab13-3]) result in performance close to that of the bag-of-words + Logistic regression model.
* Accuracy: composite 98.40% vs. logistic 98.58%
* F1 score: composite 84.36% vs. logistic 86.52%
* AUC score: composite 98.62% vs. logistic 97.48%

The diagram below shows the ROC curves for the four models that we discussed recently.
* Ngram-TfIdf-Logistic is the model in ([^colab10])
* Char-CNN is the model in ([^colab11])
* BoW-Logistic is the model in ([^colab7])
* Word2Vec-Word-Char is the composite model in ([^colab13-3]) and the one discussed above

![ROC Curves](/fakejobs/assets/images/roc_curves-2021-02-05.png)

The ROC curves demonstrate that the easy-to-interpret "bag-of-words with logistic regression" model provides satisfactory results while remaining simple.

### References
[^kaggle2]: [US Jobs on Monster.com](https://www.kaggle.com/PromptCloudHQ/us-jobs-on-monstercom)
[^colab13-3]: [Composite char and token model with Word2Vec embedding](https://github.com/r-dube/fakejobs/blob/2a0d8526029085fdd5ae1927754f19e23b6eb1c6/fj_embedding_composite.ipynb)
[^colab14]: [Colab notebook for Word2Vec embeddings](https://github.com/r-dube/fakejobs/blob/2a0d8526029085fdd5ae1927754f19e23b6eb1c6/fj_gensim_word2vec.ipynb)
[^colab10]: [N-gram + TF-IDF + Logistic regression model](https://github.com/r-dube/fakejobs/blob/main/fj_ngram_tfidf_logistic.ipynb)
[^colab11]: [Char CNN model](https://github.com/r-dube/fakejobs/blob/main/fj_char_cnn.ipynb)
[^colab7]: [Logistic regression model with bag-of-words](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
