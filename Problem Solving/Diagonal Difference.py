#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    b = int(len(a))
    slash = 0
    backslash = 0
    for i in xrange(b):
        for j in xrange(b):
            if i == j:
                backslash = backslash + a[i][j]
    for ii in xrange(b):
        for jj in xrange(b):
            if ii == b - jj-1:
                slash = slash + a[ii][jj]
    sum = abs(backslash - slash)
    return sum
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = []

    for i in xrange(n):
            a.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()