data={
'shiva@gmail.com':'123@',
'dinesh@gmail.com':'234@',
'sanjay@gmail.com':'345@',
}

email,pwd=input("Enter the email and pwd: ").split()
if data.get(email)==pwd:
    print('login successful')
else:
    print('invalid login')



items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
data=input("Enter the item:  ")

if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("avl")
    else:
        print("out of stock")
else:
    print("not avl")



