'''
def feed(l):
    for i in l:
        yield i

l = ['1','2','3','4','5']
load = feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))
print(next(load))
'''


def feed(l):
    for i in l:
        yield i

l = list(map(int,input().split()))
load = feed(l)
n = int(input())
for j in range(n):
    print(next(load))