---
title: ROC curve comparison of models
---
Given that the models' performance is similar for F1 scores, we draw some Receiver Operating Characteristic (ROC) curves to understand these models' performance at low false-positive rates.

ROC curves are explained in [^wiki1]. These curves are useful to understand classification performance across a range of false-positive rates.

[^colab9] takes the predicted probabilities of a job description being fraudulent (in the test set) and extracts a ROC curve from them. Four models are plotted: BOW + FCNN ([^colab1]), LSTM with inline embedding ([^colab3]), Transformer with position embedding ([^colab5]), and BOW + Logistic Regression ([^colab7]). The results are in the figure below:

![ROC Curves](/fakejobs/assets/images/roc_curves-2021-01-23.png)

We observe that:
* even at low false-positive rates, the performance of the four models remains close
* the LSTM model does slightly better than the other three models at most (low) false-positive rate thresholds
* the Logistic regression model does quite nicely despite its simplicity

### References
[^wiki1]: [Receiver Operating Characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
[^colab1]: [Bag-of-words with a fully-connected neural network model](https://github.com/r-dube/fakejobs/blob/main/fj_fcnn.ipynb)
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^colab5]: [Transformer model](https://github.com/r-dube/fakejobs/blob/main/fj_transformer.ipynb)
[^colab7]: [Logistic regression plus bag-of-words model](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
[^colab9]: [ROC curves creation](https://github.com/r-dube/fakejobs/blob/main/fj_roc_auc.ipynb)
