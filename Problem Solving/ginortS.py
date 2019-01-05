# Enter your code here. Read input from STDIN. Print output to STDOUT
s=raw_input()
lst = list(s)
arr1=[]
arr2=[]
arr3=[]
arr4=[]
zero=''
for i in lst:
     if 96<ord(i)<123 :
         arr1.append(i)
     elif 64<ord(i)<91:
         arr2.append(i)
     elif int(i)%2==1:
         arr3.append(i)
     elif int(i)%2==0:
        arr4.append(i)
        
        

print('{}{}{}{}'.format(''.join(sorted(arr1)),''.join(sorted(arr2)),''.join(sorted(arr3)),''.join(sorted(arr4))))