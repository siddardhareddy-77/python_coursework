#for i in range(1,20,2):


for i in range(1,11):
    if i==10:
        break
    print(i)
else:
    print("End of the numbers")



for i in range(1,11):
    if i==7:
        continue
    print(i)


l=['samrtphone','laptoop','airpods','shoes']
for i in l:
    if i=="airpods":
        continue
    print(i.center(20,"_"))
else:
    print("End")


bullets = 10
while bullets>0:
    if bullets==5:
        print("Dead")
        break
    print(bullets,"are left-You can Shoot()")
    bullets-=1
else:
    print("Game Over")