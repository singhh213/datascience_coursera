# Problem 2

# Implement a relational join as a MapReduce query
# SELECT * FROM Orders, LineItem WHERE Order.order_id = LineItem.order_id

import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)
    

def reducer(key, row):
    l=len(row)
    order = row[0]
    
    #for all the line items, append to order.
    for i in range(1, len(row)):
      mr.emit(order + row[i])
      
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)