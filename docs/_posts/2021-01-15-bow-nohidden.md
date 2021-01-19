---
title: A Neural Network with No Hidden Layers
---
Given the encouraging results with the bag-of-words (BOW) plus logistic regression model, we seek to replicate the performance with a simple neural network that mimics logistic regression.

The BOW plus logistic regression model ([^colab7]) showed that most of the signal to discriminate between fake and real jobs is in some specific words. The sequence of words is not hugely consequential. Thus, we project that a simple neural network with a BOW (represented as a dense matrix) connected to an output node with sigmoid activation would produce similar results as the logistic regression model.

We build such a model in ([^colab8]) and train it for 30 epochs. We then test the model on the held-out sample. This simple neural network model returns an accuracy of 98.70% and an F1 score of 87.18%. The results are nearly identical to those of BOW with logistic regression (accuracy 98.70% and F1 score 86.59%).

### References
[^colab7]: [Logistic regression plus bag-of-words model](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
[^colab8]: [Bag-of-words, neural network model with no hidden layer](https://github.com/r-dube/fakejobs/blob/main/fj_nohidden.ipynb)
