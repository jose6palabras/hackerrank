#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'maxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING t as parameter.
#

def maxValue(t):
    # Write your code here
    f = []
    string = t
    substrings = [string[x:y] for x, y in combinations(
            range(len(string) + 1), r = 2)]
    dic_subtrings = list(dict.fromkeys(substrings))
    for i in dic_subtrings:
        fs = len(i)*substrings.count(i)
        f.append(fs)
    return max(f)     

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
