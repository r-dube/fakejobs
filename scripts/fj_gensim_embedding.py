#!/usr/bin/env python3

from pprint import pprint as print
from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath

# Set file names for train and test data
corpus_file = "../data/fake_job_postings.csv"

model = FT_gensim(size=32)

# build the vocabulary
model.build_vocab(corpus_file=corpus_file)

# train the model
model.train(
    corpus_file=corpus_file, epochs=model.epochs,
    total_examples=model.corpus_count, total_words=model.corpus_total_words
)

print(model)


# saving a model trained via Gensim's fastText implementation
save_file = "gensim.mod"
model.save(save_file, separately=[])

print ("job" in model.wv.vocab)
print ("salary" in model.wv.vocab)
print ("learn" in model.wv.vocab)

print (model["job"])

print(model.similarity("job", "salary"))
print(model.similarity("job", "learn"))
