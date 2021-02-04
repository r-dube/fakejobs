---
title: Word2Vec experiments to match the performance of Logistic Regression
---
Since Word2Vec performed better than FastText, we experiment with hyper-parameters used to generate the embeddings.

First, we expand the unlabeled data available by obtaining and process another jobs dataset from Kaggle ([^kaggle2]).

Second, we change from the continuous bag-of-words that is the default in Word2vec to Skipgrams.

Finally, we expand the window size used by Gensim to create embedding from the default 5, to 10. The bigger window allows the Word2Vec algorithm to look at more neighboring words while generating embeddings ([^colab14]).

The above changes ([^colab13-3]) result in performance close to or above that of the bag-of-words + Logistic regression model.
* Accuracy: composite 98.40% vs. logistic 98.58%
* F1 score: composite 84.36% vs. logistic 86.52%
* AUC score: composite 98.62% vs. logistic 97.48%

### References
[^kaggle2]: [US Jobs on Monster.com](https://www.kaggle.com/PromptCloudHQ/us-jobs-on-monstercom)
[^colab13-3]: [Composite char and token model with trainable FastText embedding - updated](https://github.com/r-dube/fakejobs/blob/2a0d8526029085fdd5ae1927754f19e23b6eb1c6/fj_embedding_composite.ipynb)
[^colab14]: [Colab notebook for Word2Vec embeddings](https://github.com/r-dube/fakejobs/blob/2a0d8526029085fdd5ae1927754f19e23b6eb1c6/fj_gensim_word2vec.ipynb)
