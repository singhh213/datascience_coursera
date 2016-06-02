import sys
import json
import string
from pprint import pprint

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2], "r")
    parseFile(tweet_file)
    
def parseFile(f):

	#creates dictionary for sentiment words - scores
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
  	    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	    scores[term] = int(score)  # Convert the score to an integer.

    line = f.readline()

    # for each line, scan each word and add up its sentiment score if it exists
    #sentiment dictionary
    while line:
        data = json.loads(line)
        tweet_score = 0
        
        #checks if tweet has text property - skips over deleted tweets
        if 'text' in data:
            text = data['text'].encode('utf-8').lower()
            
            #remove punctuation
            text = text.translate(None, string.punctuation)
            
            print(text)
            for word in text.split(" "):
                if word in scores:
                    tweet_score += scores[word]
        else:
            print("no text found")

        print("Tweet Score: " + str(tweet_score))
        print("")

        line = f.readline()

if __name__ == '__main__':
    main()
