#!/bin/python

import math
import os
import random
import re
import sys


# Complete the counterGame function below.
def counterGame(n):
    def LouiseCircle(n):
        if math.ceil(math.log(n, 2)) == math.floor(math.log(n, 2)):
            n = n / 2
            if n != 1:
                RichardCircle(n)
            else:
                print 'Louise'
        else:
            n = n - 2 ** ((math.floor(math.log(n - 1, 2))))
            if n != 1:
                RichardCircle(n)
            else:
                print 'Louise'

    def RichardCircle(n):
        if math.ceil(math.log(n, 2)) == math.floor(math.log(n, 2)):
            n = n / 2
            if n != 1:
                LouiseCircle(n)
            else:
                print 'Richard'
        else:
            n = n - 2 ** ((math.floor(math.log(n - 1, 2))))
            if n != 1:
                LouiseCircle(n)
            else:
                print 'Richard'

    LouiseCircle(n)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = counterGame(n)

        # fptr.write(result+'\n')

    # fptr.close()