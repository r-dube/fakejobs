---
title: Experimentation with FastText Embedding
---
We extend our experiment with the composite token and character model to include an externally generated (non-inline) embedding.

The composite model in ([^colab12]) includes an inline embedding that was trained as part of a neural network model. Python has modules such as Gensim ([^gensim1]) that can generate an embedding from an external (presumably larger but unlabeled) dataset. We wonder if combining such an embedding with the composite model will yield good results.

### Generating the embedding
Since we don't have an additional unlabeled dataset to train the embedding on, we use the full set of job description data instead. First, we process the dataset ([^script2]) in the same manner as the token part of the composite model. Then we use Gensim to generate a FastText embedding of dimension 32 ([^script3]).

Creating the embedding in the manner described above should result in some data leakage from the test set to the training set (since the embedding is generated on the combined training and test data). As a result, we expect the new model's ([^colab13]) performance to be better than the composite model with only an inline embedding.

### Feeding the embedding to the model
We replace the composite model's embedding layer ([^colab12]) with one that uses the embedding generated above. We mark the embedding layer as trainable to mimic a real-life situation where the embeddings are developed on an unlabeled dataset separate from the labeled dataset. The rest of the composite model remains the same as before.

### Disappointing performance
The new model produces an accuracy score of 96.27%, an F1 score of 53.70%, and an AUC score of 92.74%. These results are lower than those of the composite model with inline embedding (accuracy: 98.43%, F1: 83.85%, AUC: 96.72%). The results are surprising and need further investigation.


### References
[^colab12]: [Composite char and token model](https://github.com/r-dube/fakejobs/blob/main/fj_composite.ipynb)
[^colab13]: [Composite char and token model with trainable FastText embedding](https://github.com/r-dube/fakejobs/blob/main/fj_embedding_composite.ipynb)
[^script2]: [Script to clean data](https://github.com/r-dube/fakejobs/blob/main/scripts/fj_gensim_input.py)
[^script3]: [Script to generate FastText embedding](https://github.com/r-dube/fakejobs/blob/main/scripts/fj_gensim_fasttext.py)
[^gensim1]: [gensim: FastText Model](https://radimrehurek.com/gensim_3.8.3/auto_examples/tutorials/run_fasttext.html#sphx-glr-auto-examples-tutorials-run-fasttext-py)
