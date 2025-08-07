#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    sqrl = math.sqrt(len(s))
    n = math.floor(sqrl)+1
    m = math.ceil(sqrl)
    mtx = []
    string = list(s)
    for j in range(n):
        indx1 = j*m
        indx2 = m+indx1 
        mtx.append(string[indx1:indx2])
    print(mtx)
    encoded = ''
    for i in range(m):
        for j in range(n):
            encoded = encoded + mtx[j][i]
        encoded = encoded + ' '
    print(encoded)



if __name__ == '__main__':
    s = input()
    result = encryption(s)
