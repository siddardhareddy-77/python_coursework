import re
'''
n = input()
m = input()
res = re.match(n,m)
print(res)
'''

'''
#res = re.search(r'h.t','hit hat hot')
res = re.findall(r'[0-9]','hgf2345juhygtf345676asdfgh')
#print(res.group() if res else 'no match')
print(res)
'''

'''
res = re.finditer(r'[0-9]','Hello world 32 54 87 34')
for i in res:
    print(i.group(),i.start())
'''

'''
res = re.split(r'[:;,./0]','kbdjf,hgdfdf.jfgu/jhfgu0hdgfv')
print(res)
'''


def validate_pd():
    pattern = r'^(?=.*[A-Z])(?=.*[a-z]dddd)'