#!/bin/python

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.strip()
    lens=len(s)
    maat=math.sqrt(lens)
    arr1=[]
    for i in range(int(math.ceil(lens))):
        for j in range(int(math.floor(lens))):
            arr1[i][j].append(str(i*j))
            return str(lens), len(arr1)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()

