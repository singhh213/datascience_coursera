#!/usr/bin/python

import sys
import json
import string

def main():
    tweet_file = open(sys.argv[1])
    parseFile(tweet_file)

def parseFile(f):
    
    total_wc = 0;
    freq_count = {}
    
    line = f.readline()
    
    #gets text of tweet and parses it by word. Adds word occurrence to freq_count map
    while line:
        data = json.loads(line)
        
        if 'text' in data:
            text = data['text'].encode('utf-8').lower()
            text = text.translate(None, string.punctuation)
        
        for word in text.split():
             if word not in freq_count:
                 freq_count[word] = 1
             else:
                 freq_count[word] += 1
            
             total_wc += 1
        
        line = f.readline()
    
    #prints the frequency of each word in the passed file
    for word in freq_count:
        print(word + " " + str(freq_count[word] * 1.0 / total_wc))
    
    print("")
    print("Total Word Count: " + str(total_wc))
    

if __name__ == '__main__':
    main()
            
        
                 
            