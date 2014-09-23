import json
# from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
import jsonrpclib

import pandas as pd
import ujson
import codecs
import cPickle
import nltk
from collections import Counter


#%%

class StanfordNLP:
    def __init__(self, port_number=8080):
        self.server = jsonrpclib.Server("http://localhost:%d" % port_number)

    def parse(self, text):
        return json.loads(self.server.parse(text))


#%%

pi = open('/home/paul/backup/2014-09-18_parse.pickle', 'rb')
all_results = cPickle.load(pi)
#%%
all_deps=[]
i=0
for result in all_results[0:10]:
    this_deps = []
    for sentence in result["sentences"]:
        cur_deps=[]
        keepdeps=['nn','nsubj','dobj','amod', 'agent', 'advmod', 'cop','nsubjpass']
        for dep in sentence['dependencies']:
            typ = dep[0]
            if typ in keepdeps:
                full = '_'.join(dep)
                cur_deps.append(full)
        this_deps.extend(cur_deps)
    all_deps.extend(this_deps)
dep_dict = Counter(all_deps)
#%%
dep_types = [w[0] for w in dep_dict.most_common(400)]

features = {w:0.0 for w in dep_types}

#%%

train_cases = []
test_cases = []
test_labels = []
yescount = 0
i=0
for d in data:
    i+=1
    if i % 1000==0: print i
    this_features = {w:0.0 for w in word_types}
    this_label = d[5]
   # if this_label=="unk": continue
    #print(this_label)
    for f in this_features:
        if f in d[0] and f not in label_words: this_features[f]+=1.0
    #put every 4th case in test set
    if i % 4 != 0:
        this_case = (this_features, this_label)
        train_cases.append(this_case)
    else:
        test_cases.append( (this_features) )
        test_labels.append(this_label)
#%%
print('classifying')
classifier = nltk.NaiveBayesClassifier.train(train_cases)

test_preds = classifier.batch_classify(test_cases)
corr = 0
nc = 0
print (len(test_labels))
for j in range(0, len(test_cases)):
   # print test_cases[j]
   # print test_preds[j]
    if test_labels[j] == test_preds[j]:
        corr += 1
    if test_labels[j]=='no':
        nc+=1
print classifier.show_most_informative_features(60)
print corr
print nc
print(len(train_cases))
print(len(test_cases))
