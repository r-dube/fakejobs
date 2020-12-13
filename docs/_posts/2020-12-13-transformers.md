---
title: A Transformer model from scratch
---
We create and experiment with a Transformer model and compare results with the fully-connected neural network and LSTM models.

### Why Transformers
Transformers are a relatively new class of neural network models. Like LSTM, transformers are well suited to sequenced data such as natural language text ([^trans1], [^trans2]). Given this background, we expect a Transformer model to be a relevant comparison point.

We use the Keras Transformer sample code ([^trans3]) to implement the model on Colab([^colab5]).

### Results
After training for five epochs on the full data set ([^data1]), we see that the Transformer model achieves an accuracy of 98.51% and an F1 score of 84.13%. These results are comparable with those of the bag-of-words + fully-connected neural network model ([^colab1]) and the LSTM model ([^colab3]).

### Potential future work
Given the similarity in performance across the three models, we wonder if some fraudulent jobs are, in fact, indistinguishable from real jobs, even for human experts. 

We also wonder if an ensemble of the three models would produce better results than any individual model. 

Finally, we observe that we experimented relatively little with hyper-parameters of the Transformer model. Perhaps there are (as yet undiscovered) settings that improve the Transformer model's performance over the other two models mentioned in this article.

### References
[^colab1]: [Bag-of-words with a fully-connected neural network model](https://github.com/r-dube/fakejobs/blob/main/fj_fcnn.ipynb)
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^colab5]: [Transformer model](https://github.com/r-dube/fakejobs/blob/main/fj_transformer.ipynb)
[^trans1]: [Transformers from scratch (video lecture)](https://www.youtube.com/playlist?list=PLIXJ-Sacf8u60G1TwcznBmK6rEL3gmZmV)
[^trans2]: [Transformers from scratch (blog post)](http://peterbloem.nl/blog/transformers)
[^trans3]: [Text classification with Transformer](https://keras.io/examples/nlp/text_classification_with_transformer/)
[^data1]: [Github copy of dataset from Kaggle](https://github.com/r-dube/fakejobs/blob/main/data/fake_job_postings.csv)

