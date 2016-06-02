import sys
import json
import string

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    parseFile(tweet_file)
    
def parseFile(f):

	#creates dictionary for sentiment words - scores
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
  	    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	    scores[term] = int(score)  # Convert the score to an integer.
  	
  	#dictionary for words without sentiment
    terms_dict = {}
  	
    line = f.readline()

    # for each line, scan each word and add up its sentiment score if it exists
    #sentiment dictionary
    while line:
        data = json.loads(line)
        tweet_score = 0
        word_count = 0
        no_score_words = []
        
        #checks if tweet has text property - skips over deleted tweets
        if 'text' in data:
            text = data['text'].encode('utf-8').lower()
            
            #remove punctuation
            text = text.translate(None, string.punctuation)
            
            print(text)
            for word in text.split(" "):
                if word in scores:
                    word_count = word_count + 1	
                    tweet_score += scores[word]
                else:
                    no_score_words.append(word)
        else:
            print("no text found")

        #computes avg sentiment for new terms
        avg_sentiment = 0
        if tweet_score != 0:
            avg_sentiment = tweet_score * 1.0 / word_count 
            
        print("Tweet Score: " + str(tweet_score))
        
        #adds new terms to dictionary by creating term object
        for word in no_score_words:
            if word not in terms_dict:
                term = Term(avg_sentiment)
                terms_dict[word] = term
            else:
                term = terms_dict[word]
                term.addOccurrence
                term.addScore(avg_sentiment)
                terms_dict[word] = term
                
        print("")

        line = f.readline()
        
    #print all new terms and their sentiments after file processing
    for term in terms_dict:
        print(term + " " + str(terms_dict[term].getAvg()))
        

#keeps track of occurrences and score for a term
class Term:
    
    def __init__(self, score):
        self.occurrences = 1
        self.score = score
        
    def addOccurrence(self):
        self.occurrences += 1
    
    def addScore(self, score):
        self.score += score
    
    def getAvg(self):
        return self.score / self.occurrences
    

if __name__ == '__main__':
    main()
