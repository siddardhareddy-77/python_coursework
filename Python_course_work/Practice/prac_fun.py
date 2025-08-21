'''
def add(a,b):
    return a+b
print(f'The sum is:{add(2,3)}')
'''

'''
def sqa(a,b):
    return a*a , b*b
print(sqa(4,12))
'''

'''
def circle(r):
    return 3.14*r*r
print('%.6f'%circle(3))
'''

'''
def greet(name):
    print("Hello,",name)
name = input()
greet(name)
'''

'''
def temp(deg):
    return deg*(9/5) +32
deg = float(input())
print(temp(deg))
'''

'''
def mul(a,b,c):
    return a*b*c
a,b,c=list(map(int,input().split()))
print(mul(a,b,c))
'''

'''
def interest(p,t,r):
    return (p*t*r)/100
p,t,r=list(map(int,input().split()))
print(interest(p,t,r))
'''

'''
def length(str):
    return len(str)
str = input()
print(length(str))
'''

'''
def double(l):
    for i in range(len(l)):
        l[i]=l[i]*2
    return l

l = list(map(int,input().split()))
print(double(l))
'''

'''
def sorting(s):
    return sort(s)
s=list(map(int,input().split()))
print(sorted(s))
'''


def removei(l,val):
    while val in l:
        l.remove(val)
    return l
l = list(map(int,input().split())) 
val = int(input())
print(removei(l,val))
