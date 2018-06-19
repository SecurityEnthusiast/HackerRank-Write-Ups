#!/bin/python

import sys
from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    for i in range(int(input())):
        s = raw_input()
        d[s] = d.get(s,0)+1
    print(len(d))
    for i in d:
        print(d[i]),