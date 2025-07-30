'''
n = int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:         #F
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()
'''

'''
n = 5
for i in range(n):
    for j in range(n):
        if (j==0 or i+j==n-1) and (i==0 or i==3):
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()
'''

'''
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()
'''