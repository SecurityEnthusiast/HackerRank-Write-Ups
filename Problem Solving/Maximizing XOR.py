#!/bin/python

import math
import os
import random
import re
import sys
arr=[]
# Complete the maximizingXor function below.
def maximizingXor(l, r):
    for i in range(l,r):
        for j in range(l,r):
            a=int(i) ^ int(j)
            arr.append(a)
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input())

    r = int(raw_input())
    if (r-l==1):
        result = maximizingXor(l,r+1)
    else:
        result = maximizingXor(l, r)
    print result
    fptr.write(str(result) + '\n')

    fptr.close()