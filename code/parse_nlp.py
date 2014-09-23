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
nlp = StanfordNLP()
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
dep_dict.most_common(100)
