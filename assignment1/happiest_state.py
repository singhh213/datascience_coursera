#!/usr/bin/python

import sys
import json
import string

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


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

    states_scores = {}
    
    for state in states:
        states_scores[state] = 0
    
    line = f.readline()

    # for each line, scan each word and add up its sentiment score if it exists
    while line:
        data = json.loads(line)
        tweet_score = 0
        
        #checks if tweet has text property - skips over deleted tweets
        if 'text' in data:
            text = data['text'].encode('utf-8').lower()
            
            #remove punctuation
            text = text.translate(None, string.punctuation)
            
            for word in text.split(" "):
                if word in scores:
                    tweet_score += scores[word]

        #gets user data from tweet which contains location information.
        #last two letters taken from location string as State and corresponding
        #score added to the states_score map.
        if 'user' in data:
            user = data['user']
            if 'location' in user:
                location = user['location']
                if location:
                    location = location[-2:]
                    if location in states_scores:
                        states_scores[location] += tweet_score

        line = f.readline()
        
    findHappiestState(states_scores)
    
#find happiest state by iterating through map and finding largest score
def findHappiestState(states_scores):
    happiest_state = ""
    max = -999999
    for state in states_scores:
        print(state + " " + str(states_scores[state]))
        score = states_scores[state]
        if score > max:
            max = score
            happiest_state = state
    print("")        
    print("Happiest State: " + happiest_state)
    
    
if __name__ == '__main__':
    main()    
