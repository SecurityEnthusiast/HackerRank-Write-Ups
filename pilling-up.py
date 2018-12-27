#!/usr/local/bin/python
def Analyzer(lst):

    for _ in range(len(lst)):
        #pivot = 0
        if lst[0] > lst[len(lst)-1]:
            #pivot = lst[0]
            lst.pop(0)
        elif lst[0] < lst[len(lst)-1]:
            #pivot = lst[len(lst)-1]
            lst.pop(len(lst)-1)
        else:
            #pivot = lst[0]
            lst.pop(0)
        if len(lst) == 0 :
            YN_list.append("Yes")
        else: YN_list.append("No")
    for yn in range(len(YN_list)):
        print(str(YN_list[yn]))
    print("**************************************")
    print(str(YN_list))



case_num = int(raw_input())
cube_num = []
cube_lst = []
YN_list=[]

for i in xrange(0,case_num):
    cube_num.append(int(raw_input()))
    cube_lst.append(str(raw_input().split(' ')))


for j in xrange(0,case_num):
    tuples = list( cube_lst[j])
    Analyzer(tuples)