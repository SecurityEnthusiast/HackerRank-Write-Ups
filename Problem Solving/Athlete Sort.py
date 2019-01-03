#!/bin/python
from __future__ import print_function

import math
import os
import random
import re
import sys
import time



def matrixsolver(arr,k,n,m):
    arr2=[]
    for i in range(n):
        if i<n :
            arr2.append([arr[i],i,time.time()])


    for _ in range(n):
        for j in range(n):
            if arr2[_][0][k]<arr2[j][0][k]:
                temp=arr2[_]
                arr2[_]=arr2[j]
                arr2[j]=temp
    for _ in range(n):
        for j in range(n):
            if arr2[_][0][k]==arr2[j][0][k]:
                if arr2[_][2]<arr2[j][2]:
                    temp=arr2[_]
                    arr2[_]=arr2[j]
                    arr2[j]=temp

    for l in range(n):
        for p in range(n):
            if arr[p]==arr2[l][0]:
                for t in range(m):
                    print('{} '.format(arr[int(arr2[l][1])][t]), end='')
                print ("")


if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    k = int(raw_input())

    matrixsolver(arr,k,n,m)

