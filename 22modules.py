data = {
    '1234':{'balnce':1342,'pin':123,'history':[]},
    '2348':{'balnce':3473,'pin':123,'history':[]},
    '8764':{'balnce':4567,'pin':123,'history':[]},
    '8975':{'balnce':8974,'pin':123,'history':[]}
}

acc_num = None
login_status = False

def welcome():
    print('Welcome to the ATM'.center(35,'-'))

def menu():
    print('1.Check Balance')
    print('2.')

def login(acc,pin):
    if acc in data:
        if data['pin']==pin:
            print('Login Successful')
        else:
            print('Invalid Pin')
    else:
        print("Invalid Account Number")