import pandas as pd
import ujson
import codecs
import cPickle
import nltk
import string
from collections import Counter

pi = open('/home/paul/backup/2014-09-18.pickle')
data = cPickle.load(pi)
print("opened.")
print(len(data))

#%%

data = data[0:20000]

all_toks = []
vocab_dict = {}
i=0
for d in data:
    i+=1
    if i % 1000==0:
        print i
        print len(data)
    d[0]=d[0].translate(None, string.punctuation)
    d[0] = d[0].lower()
    tokens = nltk.word_tokenize(d[0])
    d[0] = tokens
    for tok in tokens:
        all_toks.append(tok)
vocab_dict = Counter(all_toks)
#%%
stopwords = ['the','of','to',"'ll", 'be', 'is','rt']
word_types = [w[0] for w in vocab_dict.most_common(800) if w not in stopwords]
label_words=['hashsymbnothanks', 'hashsymbbettertogether', 'hashsymbvoteyes' ,'hashsymbyesscotland']
features = {w:0.0 for w in word_types if w not in label_words}

#%%

train_cases = []
test_cases = []
test_labels = []
yescount = 0
i=0
for d in data[0:20000]:
    i+=1
    if i % 1000==0: print i
    this_features = {w:0.0 for w in word_types}
    this_label = d[5]
    if this_label == 'yes':
        yescount+=1
        if yescount > 6000:
            continue

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
print classifier.show_most_informative_features(10)
print corr
print nc

