import pandas as pd
import ujson
import codecs
import cPickle

with codecs.open('/home/paul/backup/2014-09-18.json','r',encoding='utf8') as f:
        data = []
        i = 0
        rel_count = 0
        for line in f:
            relevant = False
            this_tweet = []
            i = i+1
            if i%5000 == 0:
                print i
                print(len(data))
            # removing retweets before parsing the JSON saves time
            if ("retweeted_status" in line): continue
            #bst_string = 'utc_offset":3600,
            #if (bst_string not in line) and (): continue

            thisj = ujson.loads(line)
            text = thisj["text"].encode('utf-8')
            if("http" in text.lower()): continue
            if('#indyref' in text):
                relevant = True
                rel_count +=1
            created = thisj["created_at"]
            timezone = thisj["user"]["time_zone"]
            utc = thisj["user"]["utc_offset"]
            text = text.replace('#', 'hashsymb')
            vote = "unk"
            if 'hashsymbnothanks' in text.lower(): vote = "no"
            if 'hashsymbbettertogether' in text.lower(): vote = "no"
            if 'hashsymbvoteyes' in text.lower(): vote = "yes"
            if 'yesscotland' in text.lower(): vote = "yes"
            #if 'hashsymbnothanks' in text: vote = "no"
            text = text.replace('@', 'atsymb')
            if vote == 'unk': continue
            data.append([text, created, timezone, utc, relevant, vote])

pi = open('/home/paul/backup/2014-09-18.pickle', 'w+')
cPickle.dump(data, pi)

