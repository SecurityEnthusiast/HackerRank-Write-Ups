#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr2=[]
    for i in xrange(1,5):
        for j in xrange(1,5):
            arr2.append(sum(arr[i-1][j-1:j+2])+int(arr[i][j])+sum(arr[i+1][j-1:j+2]))
    return max(arr2)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()