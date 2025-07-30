'''
date = input().split('-')           #1      DD-MM-YYYY == YYYY/MM/DD
date = date[::-1]
print('/'.join(date))
'''

'''
n = int(input())                    #2      even or odd
if n%2==0:
    print("Even Winner")
else:
    print("Odd Winner")
'''

'''
n = input().lower()
n=n.replace('a','*')                #3      relape vowels == '*'
n=n.replace('e','*')
n=n.replace('i','*')
n=n.replace('o','*')
n=n.replace('u','*')
print(n)
'''

'''
n = list(map(float,input().split()))    #4      sum and max
print(sum(n))
print(max(n))
'''

'''
username = input()
password = input()
if username=="admin" and password=="xyz123":    #5  username and password
    print("login successful")
else:
    print("access denied")
'''

'''
n = set(input().split(','))                     #6  remove duplicate
print(sorted(n))
'''

'''
n = int(input())
data = {}
max_val=0
res=''

for i in range(n):                              #7  print the name with high marks
    name,mark=input().split()
    mark=int(mark)
    if mark>max_val:
        res=name
    data[name]=mark
print(name)
'''

'''                                             #8  reverse a string
input_str = input()
output_str = ' '.join(word[::-1] for word in input_str.split())
print([output_str])
'''

'''
s = input()
s = s.replace('0','')                           #9  remove 0
print([s])
'''

'''
text = input()
text = text.replace(" ", "").lower()

frequency = {}                                  #10 frequency of each letter
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
'''