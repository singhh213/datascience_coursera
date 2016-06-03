# Problem 6
# 
# Assume you have two matrices A and B in a sparse matrix format (5x5), 
# where each record is of the form i, j, value. 
# Design a MapReduce algorithm to compute the matrix multiplication A x B

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    matrix  = record[0]
    i       = record[1]
    j       = record[2]
    value   = record[3]

    if matrix == "a":
        mr.emit_intermediate(matrix, [i,j,value])
    else:
        mr.emit_intermediate(matrix, [j,i,value])

def reducer(key, values):
    matrix_A = {}
    matrix_B = {}
    if key == "a":
       #enter matrix values
       for x in values:
           matrix_A[(x[0], x[1])] = x[2]
       for y in mr.intermediate["b"]:
           matrix_B[(y[0], y[1])] = y[2]
           
       # populate rest of matrix with zeros
       for i in range(0, 5):
           for j in range(0, 5):
               location = (i,j) 
               if location not in matrix_A.keys():
                  matrix_A[location] = 0
               if location not in matrix_B.keys():
                  matrix_B[location] = 0
                  
       # multiplication occurs here
       for i in range(0, 5):
         for j in range(0, 5):
           result = 0
           for z in range(0, 5):
               result += matrix_A[(i, z)] * matrix_B[(j, z)]
           mr.emit((i, j, result))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)