---
title: LSTM with an embedding layer
---

LSTM are a specialized form of neural networks and a classic technique for processing processing word sequences. We experiment with LSTM given that practically all of the information to differentiate betweem real and fraudulent job postings is in the text of the job postings.

### Classifier design
Since there are many unique words in the job postings, we replace the bag-of-words used in the fully-connceted neural network ([^colab1]) with word-embeddings. Word-embeddings translate each word in the job posting to more compact vector than the bag-of-words encoding. In our case, the word-embedding is learned from the training portion of the dataset. In fact, word-embedding is the first layer in our neural network design.
 
The word-embedding layer is followed by a bidirectional layer that consists of two LSTM blocks. The first LSTM block takes a set of word embeddings in the order in which the words appear in the job description. The second LSTM block takes input in the reverse order of words in the job description. The two LSTM blocks do not interact. Each unit within each LSTM block produces an output and two sets of outputs are concatenated together.

A maxpooling layer takes the maximum output of each LSTM unit (in each block) across the entire job description. This layer is fully connected to the output node.

As before, the output node uses a sigmoid activation function to output a probability that the job description is fraudulent. Also as before, we use binary cross-entropy as the loss function.

### Results
We experiment with various embedding dimension sizes (8, 16, 32) and various unit sizes in the LSTM blocks (8, 16, 32). We find that using an embedding dimension of 32 with LSTM unit sizes of 32 we get an accuracy score of 98.84% and an F1 score of 88.12% on the full dataset ([^data1]).

### Future optimization

### References
[^colab1]: [Bag-of-words with a fully-connected neural network model](https://github.com/r-dube/fakejobs/blob/main/fj_fcnn.ipynb)
[^colab3]: [LSTM model with an embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^data1]: [Github copy of dataset from Kaggle](https://github.com/r-dube/fakejobs/blob/main/data/fake_job_postings.csv)
