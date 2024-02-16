#!/bin/python3
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
string = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for j in range(m):
    for i in range(n):
        string = string + matrix[i][j]
decode = re.sub(r"(?<=\w)\W+(?=\w)", " ",string)
print(decode)