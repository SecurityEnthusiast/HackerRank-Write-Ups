# Enter your code here. Read input from STDIN. Print output to STDOUT
N,n = int(raw_input()),raw_input().split()
arr=[]
arr2=[]
for i in n:
    if (int(i)>0):
        arr.append(i)
        if (i==i[::-1]):
            arr2.append(i)
if arr==n and any(arr2):
    print('True')
else: print(False)