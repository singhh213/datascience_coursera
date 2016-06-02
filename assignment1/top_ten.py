#!/usr/bin/python

import sys
import json
import string
import operator


def main():
    tweet_file = open(sys.argv[1])
    parseFile(tweet_file)

def parseFile(f):

    hashtag_dict = {}
	
    line = f.readline()

    # for each tweet, get hashtags object and add all hashtags to the dictionary.
    while line:
        data = json.loads(line)
        tweet_score = 0
        
        #checks if tweet has text property - skips over deleted tweets
        if 'entities' in data:
            entities = data['entities']
            if 'hashtags' in entities:
                hashtags = entities['hashtags']
                for ht in hashtags:
                    text = ht[u'text']
                    if text in hashtag_dict:
                        hashtag_dict[text] += 1
                    else:
                        hashtag_dict[text] = 1
        line = f.readline()
    
    #sort dictionary in reverse order by values and then print the top ten
    sorted_x = sorted(hashtag_dict.items(), key=operator.itemgetter(1), reverse=True)
    for hashtag in sorted_x[:10]:
        print hashtag[0], hashtag[1]
    
    print(len(sorted_x))

           

if __name__ == '__main__':
    main()
