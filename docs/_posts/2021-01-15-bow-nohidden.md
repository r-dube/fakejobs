---
title: A Neural Network with No Hidden Layers
---
Given the encouraging results with the bag-of-words (BOW) with logistic regression model, we seek to replicate the performance with a simple neural network - one that mimics logistic regression.

The BOW with logistic regression model ([^colab7]) showed that most of the signal to discriminate between fake and real jobs is in some specific words. The sequence of words is not hugely consequnetial. Thus, we project that a simple neural network with a BOW (represented as a dense matrix) connected to an output node with sigmoid activation would produce similar results as the logistic regression model.

We build such a model in ([^colab8]) and train it for 30 epochs. We then test the model on the held-out sample. This simple neural network model returns an accuracy of 98.51% and an F1 score of 85.51%. The results are nearly identical to those of BOW with logistic regression (accuracy 98.58% and F1 score 85.38%).

### References
[^colab7]: [Logistic regression model with bag-of-words](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
[^colab8]: [Bag-of-words, neural network model with no hidden layer](https://github.com/r-dube/fakejobs/blob/main/fj_nohidden.ipynb)
