'''
n = int(input())
if n<=250000:
    print("No Tax")
elif 250000<n<=500000:                              #1
    print((n*5)/100)
elif 500000<n<=1000000:
    print((n*20)/100)
else:
    print((n*30)/100)
'''

'''
n = int(input())
total=0
for i in range(n):
    age=int(input())
    if 18>=age>=5 :                                 #2
        total+=100
    elif 18<age<=60:
        total+=150
    elif age>60:
        total+=120
print(total)
'''

'''
n = int(input())
if n<=100:
    print(n*1.5)
elif 100<n<=200:                                    #3
    print((100*1.5)+((n-100)*2.5))
elif 200<n<=500:
    print((100*1.5)+(100*2.5)+((n-200)*4))
else:
    print((100*1.5)+(100*2.5)+(300*4)+((n-500)*6))
'''

'''
n = int(input())
if n<=2:
    print("30")                                     #4
elif 2<n<=23:
    print(30+(n-2)*10)
else:
    print("200")
'''

'''
product = input()
n = int(input())
if n==0:
    print(product,"no stock")
elif 0<n<=10:
    print(product,"low stock")                      #5
elif 10<n<=50:
    print(product,"in stock")
else:
    print(product,"over stock")
'''

'''
n = int(input())
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:                              #6
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
'''

'''
ch = int(input())
ppl = int(input())
if ch==1:
    print(ppl*500)
elif ch==2:                                         #7
    print(ppl*1300)
elif ch==3:
    print(ppl*5000)
else:
    print("Invalid Choice")
'''

'''
n = int(input())
if 0<=n<=999:
    print("No discount")
elif 1000<=n<=4999:
    print(n*(95/100))                               #8
elif 5000<=n<=9999:
    print(n*(90/100))
else:
    print(n*(85/100))
'''


entered_pin = input()
if entered_pin == "1234" :
    print("Access Granted")
else:
    entered_pin = input()
    if entered_pin == "1234":                    #9
        print("Access Greanted")
    else:
        entered_pin = input()
        if entered_pin ==  "1234":  
            print("Access Greanted")
        else:
            print('ATM Blocked. Try Again Later')
