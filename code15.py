import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []   

    def emitIntermediate(self, key, value):
       self.intermediate.setdefault(key, [])
       self.intermediate[key].append(value)
       #print(self.intermediate)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print(item)

mapReducer = MapReduce()

def mapper(record):
    #Start writing the Map code here
   for i in record:
      values = i.strip().split(',')
      if values[0] == "Department":
        k = values[1]
        v = values[2]
        mapReducer.emitIntermediate(k, (values[0], v))
      elif values[0] == "Employee":
        k = values[2]
        v = values[1]
        mapReducer.emitIntermediate(k, (values[0], v))      

def reducer(key, list_of_values):
   #Start writing the Reduce code here
   d_list = [a[1] for a in list_of_values if a[0]=="Department"]
   e_list = [a[1] for a in list_of_values if a[0]=="Employee"]
   for i in d_list:
      for j in e_list:
         mapReducer.emit((key, j, i))   

if __name__ == '__main__':
  inputData = []
  n_max = input()
  for i in range(0, int(n_max)):
   inputData.append(input())
  #print(inputData)
  mapReducer.execute([inputData], mapper, reducer)