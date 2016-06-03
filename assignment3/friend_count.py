#Problem 3

# Consider a simple social network dataset consisting of a set of key-value pairs (person, friend)
# representing a friend relationship between two people. Describe a MapReduce algorithm to count 
# the number of friends for each person.

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)

def reducer(person, friendlist):
    mr.emit((person, len(friendlist)))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)