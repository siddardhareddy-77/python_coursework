fact = 0
n = int(input())
for i in range(2,n+1):
#for i in range(2,(n//2)+1):
    if n%i==0:
        print(i)
        fact+=1
if fact==1:
    print(n,"is prime")
else:
    print(n,"not a prime")