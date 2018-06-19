#!/bin/python

import sys

if __name__ == '__main__':
    n = int(raw_input())
    if n%2==1:
        print("Weird")
    else:
        if n<5:
            print("Not Weird")
        if 5<n<21:
            print("Weird")
        if n>20:
            print("Not Weird")