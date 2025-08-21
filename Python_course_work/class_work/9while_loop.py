email,pwd="xyz@gmail.com","xyz@123"

max_attempt = 5
cur_attempt = 1

while cur_attempt <= max_attempt:
    e=input("Enter the email: ")
    p=input("Enter the password: ")
    if e==email and p==pwd:
        print("Login successful")
        break
    else:
        print("Invalid email or password. Try again")
    cur_attempt +=1

else:
    print("Max attempts are done. Try again after 5 mins")
