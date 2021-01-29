---
title: A composite of char and token-based models
---
We continue our experimentation by creating a neural network model composed from a character and a token (word) based model,

### Inspiration for the model
Previously, we experimented with a character-based model that used CNN to extract features from the data ([^colab11], [^paper1]). 

We also experimented with an LSTM model with a learned embedding ([^colab11]) on tokens. [^paper2] suggests an alternate way to extract features from tokens and signals from a sequence of features - via a CNN block followed by an LSTM block.

[^paper3] documents a composite model that combines the character-based model with a token-based CNN-LSTM model.

### Composite model implementation
We implement the composite model ([^colab12]) from [^paper3]. The diagram below shows the network.

The token part of the model makes a few adjustments to the model in [^colab3]: in particular, we hold the maximum number of allowed tokens to 50,000 to keep memory consumption in check.

The character part of the model makes a few adjustments to the one in [^colab11] - to simplify the implementation, we encode characters previously prepared for the token portion of the model, rather than the raw text.

![Composite Model](/fakejobs/assets/images/composite_model-2021-01-29.png)

### Model performance
We observe an accuracy score of 98.28%, an F1 score of 82.84%, and an AUC score of 97.67%.

### References
[^colab3]: [LSTM model with a word-embedding layer](https://github.com/r-dube/fakejobs/blob/main/fj_lstm.ipynb)
[^colab11]: [Char CNN model](https://github.com/r-dube/fakejobs/blob/main/fj_char_cnn.ipynb)
[^colab12]: [Composite char and token model](https://github.com/r-dube/fakejobs/blob/main/fj_composite.ipynb)
[^paper1]: [Character-level Convolutional Networks for Text Classification](https://arxiv.org/pdf/1509.01626.pdf)
[^paper2]: [Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](https://arxiv.org/pdf/1506.04214.pdf)
[^paper3]: [AMSI-Based Detection of Malicious PowerShell Code Using Contextual Embeddings](https://arxiv.org/abs/1905.09538)
