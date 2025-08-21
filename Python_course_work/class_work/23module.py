from datetime import date,datetime
'''
today=date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
'''

'''
now=datetime.now()
print(now)
print(now.year)                                             #%A==day
print(now.month)                                            #%B==month name
print(now.day)                                              #%p==AM or PM
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime("%y/%m/%d"))
print(now.strftime("%B %d,%Y,%A,%p"))
'''

'''
#import sys
#import platform
import math
import random
import collections

#print(platform.system())
#print(platform.version())


print(math.sqrt(25))
print(math.pow(3,2))
print(math.fabs(-23))
print(math.floor(23.9))
print(math.ceil(54.1))


print(random.randint(1,4))


names = ['A','B','C','D','E','A','C','D',]
print(collections.Counter(names))
'''

'''
import collections

names = "python programming"

d = collections.defaultdict(int)
d['p']+=1

print(d)
'''