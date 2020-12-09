---
title: LSTM with an embedding layer
---

LSTM is a specialized form of neural network and a classic technique for processing word sequences. Given that the job descriptions are just word sequences, we experiment with LSTM for classification.

### Classifier design
Since there are many unique words in the job postings, we replace the bag-of-words used in the fully-connected neural network ([^colab1]) with word-embeddings ([^colab3]). Word-embeddings translate each word in the job posting to a more compact vector than the bag-of-words encoding. In our case, the word-embedding is learned from the training portion of the dataset. In fact, a word-embedding layer is the first layer in our neural network design.
 
The word-embedding layer is followed by a bidirectional layer that consists of two LSTM blocks. The first LSTM block takes a sequence of word-embeddings in the order in which the words appear in the job description. The second LSTM block takes input in the reverse order of words in the job description. The reverse order can help the classifier pick up information that is not accessible if the sequence is processed only in the forward direction (for example, when a word earlier in the sequence is related to a word later in the sequence). The two LSTM blocks do not interact. Each unit within each LSTM block produces an output, and the two sets of outputs (from the two blocks) are concatenated together. 

A max-pooling layer takes the maximum output of each LSTM unit (in each block) across the entire job description (that is, across the time period during which the job description is fed to the classifier). This layer is fully connected to the output node.

As before, the output node uses a sigmoid activation function to output a probability that the job description is fraudulent. Also, as before, we use binary cross-entropy as the loss function.

### Results
We experiment with different embedding dimension sizes (8, 16, 32) and various unit sizes in the LSTM blocks (8, 16, 32). We find that using an embedding dimension of 32 with LSTM unit sizes of 32, we get an accuracy score of 98.84% and an F1 score of 88.12% on the full dataset ([^data1]).

The results are comparable to those from the bag-of-words and fully-connected neural network model.

### Future optimization
We observe that the vast majority of the parameters trained in the LSTM model described above are for the word-embeddings layer. Also, each training epoch takes noticeably longer with the LSTM model than the fully-connected neural network model. We may be able to reduce the training time and potentially improve the F1 score if a robust pre-trained embedding was available.

### References
[^colab1]: [Bag-of-words with a fully-connected neural network model](https://github.com/r-dube/fakejobs/blob/main/fj_fcnn.ipynb)
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^data1]: [Github copy of dataset from Kaggle](https://github.com/r-dube/fakejobs/blob/main/data/fake_job_postings.csv)
