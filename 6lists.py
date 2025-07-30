s='''Hello
Welcome
Everyone'''
#print(s.splitlines())
S=["Hello","Welcome","Everyone"]
print(" ".join(S))

l=[1,2,3,4,5,6,7]
#print(l)
#print(l[3:7])
#print(l[-1:-5:-1])
l.insert(3,4)
print(l)
l.remove(5)
print(l)
print(l.pop(0))
print(l)
print(l.count(4))
print(sum(l))
