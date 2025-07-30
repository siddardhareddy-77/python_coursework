'''
def display(**l):
    print(l)

display(username='Shiva',email='shiva@gmail.com',password='shiva@123')
'''

'''
def greet(name,age=25):
    print(f'Hello {name}, you are {age} years old.')

greet(name='Alice')
'''

'''
def factorial(n):
    fact=1
    for i in range(1,1+n):
        fact=fact*i
    return fact

n=int(input('Enter the number: '))
for i in range(1,1+n):
    print(f"{i}!={factorial(i)}")
'''


n = int(input())
for i in range(1,n+1):
    print(n,"=",sum(range(1,n+1)))
    break
