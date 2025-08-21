'''
def update(n):
    
    print("before",n)
    n=n+10
    print("After",n)

n=10
update(n)
print("outside",n)
'''

'''
def update(n):
    
    print("before",n)               #set, list,dict are mutable, we can change
    #n=(3,4)
    k=n
    k.append(20)
    print("After",n)

#n=(1,2,3)
n=[1,2,3]
update(n)
print("outside",n)
'''

'''
n = int(input())
sum=0
for i in range(1,1+n):
    sum +=i
print(sum)
'''

'''
n = int(input())

print((n*(n+1))//2)
'''

'''
def shoot(n):
    if n==3:
        return 3
    print("before",n)
    shoot(n-1)
    print("After",n)

n = int(input())
shoot(n)
'''

'''
n = input()
sum=0
for i in n:
    sum +=int(i)
print(sum)
'''

'''
n = int(input())
def sumofnumber(n):
    if n==0:
        return 0
    return n%10 + sumofnumber(n//10)
print(sumofnumber(n))
'''


n = int(input())
a=0
b=1
for i in range(n):
    a,b = b,a+b
    print(a)