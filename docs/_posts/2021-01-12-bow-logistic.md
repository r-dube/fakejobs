---
title: Returning to Logistic Regression
---
We return to a logistic regression model to understand which job description words influence a job posting's designation as fraudulent.

### Motivation
The original bag-of-words (BOW) + fully connected neural network model (FCNN) returned an F1 score of 88.64% ([^colab1]). This score increased only modestly, if at all, with more complicated models. LSTM with embedding layer ([^colab3]) achieved an F1 score of 88.12%, and a Transformer model ([^colab5]) achieved an F1 score of 84.13%. Finally, an averaging ensemble ([^colab6]) of the three models mentioned above achieved an F1 score of 89.13%.

Given the similarity in performance between models that can use sequence information (LSTM, Transformers, ensembles including LSTM and Transformers) and the one that does not (BOW + FCNN), we reason that most of the (fraud) information resides with individual words in the job description. We create a BOW + logistic regression model ([^colab7]) to test our hypothesis.

### Getting a BOW + Logistic Regression Model to work
We had converted the sparse matrix BOW representation from Scikit-learn's CountVectorizer module to a dense matrix representation in the BOW + FCNN model. This enabled the Keras's neural network layers to receive the BOW input - these layers do not function with sparse matrix representations. 

However, using the dense matrix BOW representation causes the logistic regression module to run out of memory due to very high dimensionality. It turns out that the logistic regression module can, in fact, work with sparse matrices. Reverting to the original sparse matrix BOW output of the CountVectorizer allows the experiment to proceed.

Finally, instead of using counts in the BOW representation, we switch to a binary mode (that records the presence or absence of a word). Such a model would  be simpler to interpret.

### Results of Logistic Regression Model
The logistic regression model trains faster in comparison to the neural network models and returns an accuracy of 98.70% and an F1 score of 86.59%

### Top-20 Words Indicating Fraud
We trace back the largest coefficients in the logistic regression model (indicating the most influential words in fraudulent job postings) to the job postings' original words. We list the 20 most significant words from the training data below. The first number represents the index in the dictionary produced by the CountVectorizer. The second number is the logistic regression coefficient of the corresponding word. Finally, the third field represents the word itself.
* 8876 0.6258794722749936 balance
* 73348 0.6333128423457315 send
* 25611 0.6259285387198736 duration
* 38004 0.6434919556502703 hospital
* 90433 0.75822867725062 wages
* 51049 0.7556025983045982 money
* 54480 0.7290765727550464 oil
* 26515 0.7340161687538614 egovernment
* 939 0.6560803983381377 28
* 6562 0.7140744759683485 aptitude
* 90601 0.6543170280066289 warsaw
* 54398 0.7694429585002532 offshore
* 2587 1.0494498113942459 accounting
* 83983 0.8756074645931318 timejob
* 1 0.7794737530953701 000
* 45978 1.4066493742729074 link
* 70901 1.2020262877494345 rohan
* 3537 0.9737890429754346 administrative
* 8060 0.8073265859315331 au
* 25832 1.0480087026327678 earn


Some of the top-20 words make intuitive sense. Words such as "money," "earn," and "wages," match one's intuition of a fake job description. However, other words are surprising. "rohan" is a first name, and words such as "aptitude" and "duration" do not seem out of place in a job description. 

In any case, the BOW + logistic regression model enables interpretation of the results, which is not easily feasible with the neural network models.

### References
[^colab1]: [Bag-of-words with a fully-connected neural network model](https://github.com/r-dube/fakejobs/blob/main/fj_fcnn.ipynb)
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^colab5]: [Transformer model](https://github.com/r-dube/fakejobs/blob/main/fj_transformer.ipynb)
[^colab6]: [Ensemble models](https://github.com/r-dube/fakejobs/blob/main/fj_ensemble.ipynb)
[^colab7]: [Logistic regression model with bag-of-words](https://github.com/r-dube/fakejobs/blob/main/fj_bow_logistic.ipynb)
