#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    Alice=0
    Bob=0
    for i in range(0,len(a)):
        if a[i]>b[i]:
            Alice +=1
        elif a[i]<b[i]:
            Bob+=1
    out=[Alice,Bob]
    return(out)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()y