
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
categories = [cat.strip() for cat in input("Enter Categories (comma-separated): ").split(',') if cat.strip()]
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)
discount_percentage = float(input("Enter Discount Percentage: "))

print("\n--- Product Details in Various Formats ---\n")
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")
print("Product Discount: %.2f%%" % discount_percentage)
print(f"Product Name: {product_name}")
print(f"Price: {price:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")

print("\nCategories:", categories)
print("Stock details (Available, Sold):", stock_details)
