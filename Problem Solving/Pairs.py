#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k,arr):
    counter=0
    counter = len(set(arr) & set(i + k for i in arr))
    return counter 

if __name__ == '__main__':
    
    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())
    
    result = pairs(k, arr)
    print result