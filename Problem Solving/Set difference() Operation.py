# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=input()
set1=set(raw_input().split())
n2=input()
set2=set(raw_input().split())
count=0
diff=set1.difference(set2)
for i in diff:
    count=count+1
print(count)