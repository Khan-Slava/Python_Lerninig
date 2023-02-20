'''for i in range (1,10):
    a=i
    while a>=1:
        print("*", end="")
        a-=1
    print()



import random
s=[]
list= [10,2,'e']
for i in range (1,10):
    s.append(i)

print(s)
for i in enumerate(list):
    print(i)

print(random.randrange(1,100))
'''



#1
'''
a=int (input("input a: "))
b=int(input("input b: "))
if (a>=b):
    temp=b
    a=b
    b=temp
for i in range(a,b+1):
    print(i,"; ")
'''
#2
'''
a=int (input("input a: "))
b=int(input("input b: "))
if (a<=b):
    for i in range(a,b+1):
        print(i,"; ")
else:
    for i in range(a+1,b,-1):
        print(i-1,"; ")
'''
#3

a=int (input("input a: "))
b=int(input("input b: "))
while a<=b :
    while a%2==1 and a<=b:
        print(a)
        a+=1
    a+=1


#4
'''
import random
n=int (input("input n: "))
sum=0
last_sum=0
for i in range(0,n+1):
    sum+=i

for i in range(1,n):
    last_sum+=int(input())
print("потеряна: ", sum-last_sum)

'''