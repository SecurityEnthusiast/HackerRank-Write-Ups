#!/bin/python
from __future__ import print_function
import os
import sys
import math

# Complete the solve function below.
"""
def solve(n,arr):
    for i in arr:
        arr2=[]
        for j in range(0,i+1):
            C=int(math.factorial(i)/((math.factorial(j)*math.factorial(i-j))))
            C=str(C)
            C=C[-9:]
            arr2.append(int(C))
        print(*arr2, sep=' ')

"""
def solve(n,arr):
    i=int(arr[0])
    index=0
    while i in arr:
        arr2=[]
        j=0
        while j<i+1:
            C=str(int(math.factorial(i)/((math.factorial(j)*math.factorial(i-j)))))[-9:]
            arr2.append(int(C))
            j=j+1
        print(*arr2, sep=' ')
        index=index+1
        if index<len(arr):
            i=int(arr[index])
        else:
            return 1



if __name__ == '__main__':


    t = int(input())
    arr=[]

    for t_itr in range(0,t):
        arr.append(int(input()))
    result = solve(t,arr)