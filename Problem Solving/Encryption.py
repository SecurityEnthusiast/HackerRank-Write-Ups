#!/bin/python

from __future__ import print_function
import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    encryption.daemon = True
    s=s.replace(" ", "")
    lens=len(s)
    maat=math.sqrt(lens)
    floor=int(math.floor(maat))
    ceil=int(math.ceil(maat))

    arr1=[]
    string = ''
    counter = 0

    for i in range(floor):
        for l in range(ceil+1):
            if len(s) > len(arr1):
                arr1.append(s[counter])
                counter+=1
    
    for l in range(ceil):
        string = ''
        for i in range(floor+1):
            if l+i*ceil < len(arr1):
                string = string + str(arr1[l+i*ceil])
        print(string,end=' ')

    return 1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    #fptr.write(result + '\n')

    #fptr.close()

