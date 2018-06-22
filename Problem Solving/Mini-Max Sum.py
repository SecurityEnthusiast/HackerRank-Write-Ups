#!/bin/python

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    thirdarr=[]
    for i in range(len(arr)):
        secarr=arr[:]
        secarr.pop(i)
        thirdarr.append(sum(secarr))
    m=max(thirdarr)
    mn=min(thirdarr)
    print mn,m

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)