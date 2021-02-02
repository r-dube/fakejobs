---
title: More Experimentation with Embeddings
---
We investigate the poor performance of the composite model with external embeddings.

### Changing embedding generation
First, we train the embedding for longer - 15 epochs in ([^colab13-2]) compared to the default 5 epochs in ([^colab13]). The embedding size remains at 32 and the embedding is trained on the corpus of cleaned text as before.

### Changing the model hyperparameters
Second, we prevent the embedding layer from being trained further during the composite model's training.

Finally, we train the composition model for longer: 15 epochs rather than previous 7 epochs.

### New results with FastText
The results with the new model are respectable and notably better than the older model: accuracy of 97.24% (vs. 96.27%), F1 score of 71.32% (vs. 53.70%), AUC score of 95.55% (vs 92.74%).

### Using Word2vec instead of FastText
We find that the model's performance improves when we switch from using FastText to Word2vec while holding all the other hyperparameters constant. We get: accuracy of 97.99%, F1 score of 81.12%, AUC score of 97.31%.

Clearly the classification performance of the model is very sensitive to the quality of the training. Unfortunately, there does not appear to be an easy way to judge the quality of an embedding on esoteric corpora ([^word2vec]).

### References
[^colab13]: [Composite char and token model with trainable FastText embedding](https://github.com/r-dube/fakejobs/blob/c7fe25acbe28a08949f8a35003539cf7ee5687a2/fj_embedding_composite.ipynb)
[^colab13-2]: [Composite char and token model with trainable FastText embedding - updated](https://github.com/r-dube/fakejobs/blob/94eab0adc2e5309d6fdb3a8591abb68a3f16f7d2/fj_embedding_composite.ipynb)
[^word2vec]: [Word2vec and friends](https://www.youtube.com/watch?v=wTp3P2UnTfQ)
