#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # [4,8,2,1,5,3]
    price_map = {}
    for i, price in enumerate(arr):
        complement = m - price
        if complement in price_map:
            return [price_map[complement] + 1, i + 1]
        price_map[price] = i
    return []

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())# amount of money to spend 

        n = int(input().strip())#number of flavors

        arr = list(map(int, input().rstrip().split())) #cost of each flavor

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
