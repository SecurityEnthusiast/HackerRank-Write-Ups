#!/bin/python

total= 0;k = input()
fields = raw_input().strip().split()
for i in range(k):
    total = total+int(raw_input().split()[fields.index('MARKS')])
print float((total)/k)