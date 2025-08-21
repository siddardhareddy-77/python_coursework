data = {"balance": 34566, "history": []}

def current_balance():
    print(f'Current Balance: ₹{data["balance"]}')

def deposit():
    amount = int(input("Enter the amount to deposit: "))
    if amount % 100 == 0 or amount % 500 == 0:
        data['balance'] += amount
        data['history'].append(f"Deposited ₹{amount}")
        print(f"Deposited ₹{amount}")
    else:
        print("Invalid denomination")

def withdraw():
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 100 == 0 or amount % 500 == 0:
        if amount <= data['balance']:
            data['balance'] -= amount
            data['history'].append(f"Withdrawn ₹{amount}")
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")
    else:
        print("Invalid denomination")

def show_history():
    if data['history']:
        print("Transaction History:")
        for item in data['history']:
            print("-", item)
    else:
        print("No transactions yet.")

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        current_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        show_history()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
        