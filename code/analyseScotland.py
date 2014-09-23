import pandas as pd
import ujson
import codecs
import cPickle
import nltk
from collections import Counter

pi = open('/home/paul/backup/2014-09-18.pickle')
data = cPickle.load(pi)
print("opened.")

data = data[0:10000]
#%%

vocab =set()
texts = [d[0] for d in data]

all_toks = []
word_dict = {}
i=0
for t in texts:
    i=i+1
    if(i%1000==0): print i
    tokens = nltk.word_tokenize(t)
    for tok in tokens:
        all_toks.append(tok)
word_dict = Counter(all_toks)


