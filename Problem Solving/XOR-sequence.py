#!/bin/python

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.

def xorSequence(n):
    if(n%8==0 or n%8==1):
        return n
    elif(n%8==2 or n%8==3):
        return 2
    elif(n%8==4 or n%8==5):
        return n+2
    else:
        return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())
    for q_itr in range(q):
        lr = raw_input().split()

        l = int(lr[0])

        r = int(lr[1])

        #fptr.write(str(xorSequence(l,r))+'\n')

        print(xorSequence(l-1)^xorSequence(r)) 


    #fptr.close()
