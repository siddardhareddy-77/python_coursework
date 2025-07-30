data = {
    1: {'name': 'Rice', 'Price': '60'},
    2: {'name': 'Wheat', 'Price': '45'},
    3: {'name': 'Sugar', 'Price': '40'},
    4: {'name': 'Milk', 'Price': '25'},
    5: {'name': 'Eggs', 'Price': '70'},
    6: {'name': 'Cooking Oil', 'Price': '130'},
    7: {'name': 'Tea Powder', 'Price': '90'},
    8: {'name': 'Salt', 'Price': '20'},
    9: {'name': 'Bread', 'Price': '30'},
    10: {'name': 'Soap', 'Price': '50'}
}

# Display the items
for i in range(1, 11):
    print(f'{i}. {data[i]["name"].ljust(15)} : {data[i]["Price"]}')

# Get user input
items = list(map(int, input("Enter the item indexes (space separated): ").split()))
print("Selected items:", items)

total = 0
ids = set()
for i in items:
    if i not in ids:
        count = items.count(i)
        price = int(data[i]["Price"])
        subtotal = price * count
        print(f'{data[i]["name"]} - {count} * {price} = {subtotal}')
        total += subtotal
        ids.add(i)

print("Total Bill:", total)
