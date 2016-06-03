# Problem 4

# The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
# Implement a MapReduce algorithm to check whether this property holds. 
# Generate a list of all non-symmetric friend relationships.

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)

def reducer(person, friends):
    for possible_friend in friends:
       if possible_friend not in mr.intermediate.keys() or person not in mr.intermediate[possible_friend]:
          mr.emit((person, possible_friend))
          mr.emit((possible_friend, person))
         
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)