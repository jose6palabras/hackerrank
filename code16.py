import sys
from collections import OrderedDict

class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.intermediate2 = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emitIntermediate2(self, key, value):
        self.intermediate2.setdefault(key, [])
        self.intermediate2[key].append(value)

    def emit(self, value):
        self.result[value[0]][value[1]] = value[2]

    def execute(self, matrix1, matrix2, mapper, reducer):
        n = len(matrix1)
        m = len(matrix2[0])
        for i in range(0, n):
            self.result.append([0] * m)

        mapper(matrix1, matrix2)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for key in self.intermediate2:
            reducer2(key, self.intermediate2[key])        

        for i in range(0, n):
            row = ""
            for j in range(0, m):
                row += str(self.result[i][j]) + " "
            print(row)

def mapper(matrix1, matrix2):
    # Start writing the Map code here
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            mapReducer.emitIntermediate(j, ("m1", i, matrix1[i][j]))
    for j in range(len(matrix2)):
        for k in range(len(matrix2[j])):
            mapReducer.emitIntermediate(j, ("m2", k, matrix2[j][k]))    

def reducer(key, list_of_values):
    # Start writing the Reduce code here
    m1 = []
    m2 = []
    for i in list_of_values:
        if i[0] == "m1":
            m1.append((i[1], i[2]))
        elif i[0] == "m2":
            m2.append((i[1], i[2]))
    for a in m1:
        for b in m2:
            key2 = (a[0], b[0])
            mapReducer.emitIntermediate2(key2, a[1]*b[1])
            
def reducer2(key, values):
    i = key[0]
    j = key[1]
    val = sum(values)
    mapReducer.emit((i, j, val))

if __name__ == '__main__':
    testcases = int(input())
    for _ in range(testcases):
        mapReducer = MapReduce()
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        matrix1 = []
        matrix2 = []
        
        for i in range(row):
            read_row = sys.stdin.readline().strip()
            matrix1.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix1[i].append(int(row_elems[j]))
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        
        for i in range(row):
            read_row = sys.stdin.readline().strip()
            matrix2.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix2[i].append(int(row_elems[j]))        
        mapReducer.execute(matrix1, matrix2, mapper, reducer)