#!/bin/python


a=input()
b=input()
m=input()

if 1<=a<=10 and 1<=b<=10 and 2<=m<=1000:
    print(a**b)
    print((a**b)%m)