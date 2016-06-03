# Problem 5
# Consider a set of key-value pairs where each key is sequence id and each value is a 
# string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
# Write a MapReduce query to remove the last 10 characters from each string of nucleotides,
# then remove any duplicates generated.

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    
    seq = record[1]
    trimmed = (seq)[:-10]
    mr.emit_intermediate(trimmed, record[0])

def reducer(sequence, id):
    mr.emit(sequence)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)