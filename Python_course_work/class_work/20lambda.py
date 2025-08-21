'''
n = int(input())
sq = lambda n: n*n
print(sq(n))
'''

'''
def squares(l):
    for i in range(len(l)):
        l[i]=l[i]**2
    return l
'''
'''
l=[1,2,3,4,5]
#print(squares(l))

sqa = list(map(lambda i: i**2, l))
print(sqa)
'''

'''
l = ['pen','book','pencil']
k = tuple(l)
print(k)
'''

'''
n = int(input())

leap = lambda n: n%4==0 and (n%100!=0 or n%400==0)
print(leap(n))
'''

'''
l = ["car", "elephant", "cat"]
sortedlist = lambda l: sorted(l)
print(sortedlist(l))
'''


n = [2,3,4,5,6,79,9,24]
divisibleby3 = lambda n: set(filter(lambda n: n%3==0,n))
print(divisibleby3(n))