
#1.Arithmetic operators

a=10
b=20
print(a+b)      #addition
print(a/b)      #division
print(a*b)      #multiplication
print(a//b)     #flodiv
print(a%b)      #mod
print(a**b)     #exp(**)


#2.Comparision operators

c=30
d=40
print(c==d)     #equal
print(c!=d)     #not equal
print(c<d)      #lessthan
print(c>d)      #greater
print(c<=d)     #less or equal
print(c>=d)     #greater or equal


#3.Assignment Operators

e=30
e+=20
print("e+=",e)      #50
e-=10
print("e-=",e)      #40
e*=5
print("e*=",e)      #200
e/=10
print("e/=",e)      #20
e**=2
print("e**=",e)     #400
e//=10
print("e//=",e)     #40
e%=5
print("e%=",e)      #0


#4.Logical OPerators

x=40
y=20
print("and:",x%10==0 and y%10==0)
print("or:",x%10==0 or y%5==0)


#5.Membership Operators

n="River"
print("R" in n)
names = ['sai','ram']
print("sai" in names)
v = "aeiou"
print(n in v)


#6.Identity Operators

l = [1,2,3,4]
b = [1,2,3,4]
print(l==b)
a=b
print(a)
print(id(b))
print(id(a))
print(id(l))
print(a is not b)
print(l is not b)


#7.Bitwise Operators

print(5&3)      #and
print(5/3)      #or
print(5^3)      #xor