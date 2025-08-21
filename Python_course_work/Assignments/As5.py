class User:
    def __init__(self, username, password, email):
        self.__username = username        # encapsulation
        self.__password = password
        self.email = email

    def get_username(self):
        return self.__username

    def verify_password(self, password):
        return self.__password == password


class Item:
    def __init__(self, name, item_type, price):
        self.name = name
        self.item_type = item_type
        self.price = price


class Cart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, item):
        self.items.append(item)

    def apply_discount(self, discount_percent):
        self.discount = discount_percent

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        if self.discount > 0:
            total -= total * (self.discount / 100)
        return total


# ----- Abstraction + Inheritance + Polymorphism -----
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay() method")


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"✅ Paid ₹{amount} using Credit Card"


class UPIPayment(Payment):
    def pay(self, amount):
        return f"✅ Paid ₹{amount} using UPI"


class CashOnDelivery(Payment):
    def pay(self, amount):
        return f"✅ Order of ₹{amount} placed with Cash on Delivery"


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("=== Welcome to Amazon Website ===")

    # User details
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    user = User(username, password, email)
    print(f"Hello {user.get_username()}, your account is created!\n")

    # Cart
    cart = Cart()
    n = int(input("Number of items: "))

    for i in range(n):
        name = input(f"Enter item {i+1} name: ")
        item_type = input("Enter item type: ")
        price = float(input("Enter item price: "))
        cart.add_item(Item(name, item_type, price))

    discount = float(input("Enter discount percentage (0 if none): "))
    cart.apply_discount(discount)

    total = cart.calculate_total()
    print(f"\n🛒 Total after discount: ₹{total}\n")

    # Payment choice
    print("Choose payment method: ")
    print("1. Credit Card\n2. UPI\n3. Cash on Delivery")
    choice = int(input("Enter choice (1-3): "))

    if choice == 1:
        payment = CreditCardPayment()
    elif choice == 2:
        payment = UPIPayment()
    else:
        payment = CashOnDelivery()

    print(payment.pay(total))
    print("\n🎉 Thank you for shopping with Amazon!")
