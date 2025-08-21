
n = int(input())
if n>0:
    print("positive")
else:
    print("negative")

if n%2==0:
    print("even")
else:
    print("odd")

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a>b:
    print(a,"is greater than",b)
    #print(f"{a} is greater than {b}")
elif a==b:
    print(a,"is equal to",b)
else:
    print(b,"is greater than",a)



n = int(input("n = "))
if n%2==0 and n%3==0:
    print(n,"is divisible by 2&3")
elif n%2==0:
    print(n,"is divisible 2")
elif n%3==0:
    print(n,"is divisible 3")
else:
    print()