#!/usr/bin/env python3

# For gensim
from pprint import pprint as print
from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath

# Set file names
corpus_file = ".gensim-cache/fj_processed.txt"
# corpus_file = ".gensim-cache/fj_small_processed.txt"
save_file = ".gensim-cache/gensim.mod"

# Initialize the model
model = FT_gensim(size=32)

# build the vocabulary
model.build_vocab(corpus_file=corpus_file)

# train the model
model.epochs = 15
model.train(
    corpus_file=corpus_file, epochs=model.epochs,
    total_examples=model.corpus_count, total_words=model.corpus_total_words
)
print(model)

# saving a model trained via Gensim's fastText implementation
model.save(save_file, separately=[])

# run some basic tests on the model
print ("job" in model.wv.vocab)
print ("salary" in model.wv.vocab)
print ("learn" in model.wv.vocab)

# print vector representaion
print (model["job"])

# test similarity
print(model.similarity("job", "salary"))
print(model.similarity("job", "learn"))
print(model.similarity("job", "the"))
