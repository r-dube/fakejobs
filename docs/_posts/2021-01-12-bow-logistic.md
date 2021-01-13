---
title: Returning to Logistic Regression
---

The original bag-of-words (BOW) + fully connected neural network model (FCNN) returned an F1 score of 88.64% ([^colab1]). This score increased only modestly, if at all with more complicated models. LSTM with embedding layer ([^colab3]) achieved an F1 score of 88.12% and a Transformer model ([^colab3]) achieved an F1 score of 84.13%. Final an averaging ensemble ([^colab6]) of the three models mentioned above achieved an F1 score of 89.13%.

Given the similarity in performance between models that can use sequence information (LSTM, Transformers, ensembles including LSTM and Transformers) and the one that does not (BOW + FCNN), we reason that most of the (fraud) information resides with individual words in the job description. We create a BOW + logistic regression model ([^colab7]) to test our hypothesis.

### Getting a BOW + Logistic Regression Model to work
We had converted the sparse matrix BOW representation from Scikit-learn's CountVectorizer module to a dense matrix representation in the BOW + FCNN model. This was to enable the Keras's neural network layers to receive the BOW input - these layers do not function with sparse matrix representations. 

However, using the dense matrix BOW representation, causes the logistic regression module to run out of memory on account of very high dimensionality. It turns out that the logisic regression module can, in fact, work with sparse matrices. Reverting to the original sparse matrix BOW output of the CountVectorizer allows the experiment to proceed.

### Results of Logistic Regression Model
The logisic regression model trains faster in comparison to the neural network models and returns an accuracy of 98.58% and an F1 score of 85.38%

### Top-20 Words Indicating Fraud
We trace back the largest coefficients in the logistic regression model (indicating the words that are the most influential in fraudulent job postings) to the original words in the job postings. We list the 20 most influential words from the training data below. The first number represents the index in the dictionary produced by the CountVectorizer. The second number is the logistic regression coefficient of the corresponding word. Finally, the third field represents the word itself.
* 33685 0.583666549778054 forward
* 90601 0.5880771388570726 warsaw
* 50275 0.5922453583229651 migration
* 58424 0.5894725690060855 personable
* 25611 0.6014009057248951 duration
* 3537 0.6200141194192783 administrative
* 85478 0.6097342380566507 trends
* 2560 0.6230277267508464 accountant
* 51410 0.6342872633589646 motivated
* 51049 0.6430812625819265 money
* 8060 0.6540206821739426 au
* 25832 0.7034693991546753 earn
* 2420 0.7909873621854235 accion
* 28288 0.7036004048677369 entry
* 90433 0.696350398561821 wages
* 70901 1.2517113334375831 rohan
* 6562 0.8661454561535944 aptitude
* 53381 0.6744264060592281 northwestern
* 45978 1.0131995590683975 link
* 4869 0.6697178300384368 american

Some of the top-20 words make intuitive sense. Words such as "money", "earn", "wages" and "motivated" match one's intuition of a fake job description. However, other words are surprising. "rohan" is a first name and words such as "aptitude" and "trends" do not seem out of place in a job description. 

In any case, the BOW + logistic regression model enables interpretation of the results - something that is not easily feasible with the neural network models.

### References
[^colab1]: [Bag-of-words with a fully-connected neural network model](https://github.com/r-dube/fakejobs/blob/main/fj_fcnn.ipynb)
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^colab5]: [Transformer model](https://github.com/r-dube/fakejobs/blob/main/fj_transformer.ipynb)
[^colab6]: [Ensemble models](https://github.com/r-dube/fakejobs/blob/main/fj_ensemble.ipynb)
[^colab7]: [Logistic regression model with bag-of-words](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
