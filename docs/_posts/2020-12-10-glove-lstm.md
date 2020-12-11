---
title: LSTM with a pre-trained embedding layer
---
We experiment with a pre-trained word-embedding layer as part of an LSTM model.

### Changes to the LSTM model
Since the word-embedding layer added substantial training time, we replaced the embedding-layer in the previously discussed LSTM model ([^colab3]) with a pre-trained word-embedding ([^glove1]). 

We use one of the smaller-dimension embeddings from those available as the files containing the vector representations of words are very large (150MB to 2GB). Fewer dimensions translate to smaller files making experimentation feasible. 

### Results
The resulting network ([^colab4]) has far fewer parameters to be trained. As a result training proceeds faster. Unfortunately the F1 score achieved by the new model tops out at 79.12% on the full dataset ([^data1]).

### Conclusions
While the training is faster, as expected, the inferior results (relative to the LSTM network with a trainable embedding layer) seem surprising. The poorer results could be due to a couple of reasons. 

First, we chose the smallest possible embedding (50 dimensions) when larger embeddings (upto 300 dimensions) were available. We chose the smaller embedding to keep the file sizes manageable. It is possible that higer dimensional embeddings would have resulted in better performance.

Second, we chose an embedding derived from a smaller vocabulary (400K words) when larger vocabularies (2.2M) were available. Again, this was to keep files small, but may have resulted in a loss of usable information from the job descriptions.

Third, the pre-trained embedding was obtained by training on general text such as that in Wikipedia. The data in our dataset - job descriptions - is specialized and may be dissimilar enough from general text that the pre-trained embedding reduces the information available to the LSTM model.

### References
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^glove1]: [Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
[^colab4]: [LSTM model with a pre-trained word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_glove_lstm.ipynb)
[^data1]: [Github copy of dataset from Kaggle](https://github.com/r-dube/fakejobs/blob/main/data/fake_job_postings.csv)
