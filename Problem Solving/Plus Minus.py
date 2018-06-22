#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in range(len(arr)):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg += 1
        else:
            zer+=1
    print(float(pos)/len(arr)),'\n',(float(neg)/len(arr)),'\n',(float(zer)/len(arr))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)