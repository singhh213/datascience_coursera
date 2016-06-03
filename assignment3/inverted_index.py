# Problem 1

# Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word 
# is associated with a list of the document identifiers in which that word appears.

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(word, keys):
    docs = []
    for v in keys:
        docs.append(v)
    mr.emit((word, docs))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
    