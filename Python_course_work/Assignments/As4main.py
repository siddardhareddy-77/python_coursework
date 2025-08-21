import As4

def menu():
    print('--------Programmes Menu--------')
    print("1. Check File Exists")
    print("2. Phone Number Validator")
    print("3. Diamond Pyramid")
    print("4. Decimal to Binary")
    print("5. Find the Power of a number")
    print("6. Group Words With Same Set of Characters")
    print("7. Print the first n prime numbers")
    print("8. Volume of circle")
    print("9. Find All Palindrome Numbers in Range")
    print("10.Merge Dictionaries")
    print("0. Exit")
    print("-------------------------------")

def main():
    while True:
        menu()
       
        choice = int(input("Enter your choice: "))
       
        if choice == 0:
            print("Thank You")
            break
        elif choice == 1:
            As4.checkfileexists()   
        elif choice == 2:
            As4.phone_number_validator()
        elif choice == 3:
            As4.diamond_pyramid()
        elif choice == 4:
            As4.decimal_to_binary()
        elif choice == 5:
            As4.findthepowerofnumber()
        elif choice == 6:
            As4.same_set_characters()
        elif choice == 7:
            As4.primes()
        elif choice == 8:
            As4.volumeofcircle()
        elif choice == 9:
            As4.palindrome()
        elif choice == 10:
            As4.mergedictionaries()
        
        else:
            print("Invalid choice! Please try again.\n")


main()
