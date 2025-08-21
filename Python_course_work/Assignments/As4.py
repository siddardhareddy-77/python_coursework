def checkfileexists():  
    print("\n1. Check File Exists")
    print('''
file_path = input()
try:
    with open(file_path):
        pass
    print("File exists.")
except FileNotFoundError:
    print("File does not exist.")

#Example 1:
input:  python.txt
output: File exists.
          
#Example 2:
input:  jnhbgfd.txt
output: File does not exist.

#Explination: The program checks if the specified file path exists and prints a confirmation message accordingly.  
''')

def phone_number_validator():
    print("\n2. Phone Number Validator")
    print('''
def validate_phone_number(number):
    if len(number) == 10 and number.isdigit() and number[0] in '6789':
        return True
    return False

phone = input()

if validate_phone_number(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
     
#Example 1:
input:  4329776664
output: Invalid phone number
          
#Example 2:
input:  8566637908
output: Valid phone number

#Explination: This function checks if the input is a 10-digit number 
              starting with 6, 7, 8, or 9 to validate it as a phone number.
''')

def diamond_pyramid():
    print("\n3. Diamond Pyramid")
    print('''
num=int(input(""))   
for i in range(1,num+1):   
    print(" "*(num-i),end="")   
    for j in range(1,i+1):   
        print("*",end=" ")   
    print()   
for p in range(1,num):   
    print(" "*p,end="")
    for q in range(1,num+1-p):   
        print("*",end=" ")   
    print()

#Example 1:
input:  5
output:      
                *
               * *
              * * *
             * * * *
            * * * * *
             * * * *
              * * *
               * *
                *
               
#Explination:  This code prints a symmetrical diamond-shaped pattern of stars using two loops.
                 one for the upper pyramid and one for the inverted lower pyramid.
''')


def decimal_to_binary():
    print("\n4. Decimal to Binary")
    print('''
decimal = int(input())
binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

print(binary)
          
#Example 1:
input:  4
output: 100
          
#Example 2:
input:  10
output: 1010

#Explination: This code converts a decimal number to its binary equivalent by repeatedly dividing by 2 and
              storing remainders in reverse order.
''')


def findthepowerofnumber():
    print("\n5. Find the Power of a number")
    print('''
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = base ** exponent
print(f"{base}^{exponent} = {result}")
          
#Example 1:
input:  Enter base: 2
        Enter exponent: 3
          
output: 2^3 = 8
          
#Example 2:              
input:  Enter base: 3
        Enter exponent: 3
          
output: 3^3 = 27

#Explination: This code calculates the power of a number by raising the base to the given exponent using **.
          
         ''')



def same_set_characters():
    print("\n6. Group Words With Same Set of Characters")
    print('''
from collections import defaultdict

def group_words(words):
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(set(word)))  # unique characters in sorted order
        groups[key].append(word)

    return list(groups.values())

words = ["bat", "tab", "tap", "pat", "tba", "apt", "cat"]
result = group_words(words)

for group in result:
    print(group)
          
#Example :
 
output: ['bat', 'tab', 'tba']
        ['tap', 'pat', 'apt']
        ['cat']
 
#Explination: This code groups words that share the same unique set of characters using a dictionary.
''')


def primes():
    print("\n7. Print the first n prime numbers")
    print('''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1
n = int(input("Enter how many prime numbers to print: "))
print_n_primes(n)
          
#Example 1:
input:  5
output: 2 3 5 7 11
          
#Example 2:
input:  10
output: 2 3 5 7 11 13 17 19 23 29 

#Explination: This code prints the first n prime numbers by checking each number for primality and
              counting until the desired number is reached
''')


def volumeofcircle():
    print("\n8. Volume of circle")
    print('''
import math

radius = float(input())

volume = (4 / 3) * math.pi * radius ** 3
print(volume)

#Example 1:
input:  3
output: 113.097
          
#Example 2:
input:  5
output: 523.598

#Explination: The program calculates and prints the volume of a sphere using the formula (4/3) * π * radius^3.
''')


def palindrome():
    print("\n9. Find All Palindrome Numbers in Range")
    print('''
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def palindrome_in_range(start, end):
    for num in range(start, end + 1):
        if is_palindrome(num):
            print(num, end=' ')

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Palindrome numbers from {start} to {end}:")
palindrome_in_range(start, end)

#Example 1:
input:   100
         150
output:  101 111 121 131 141
          
#Example 2:
input:    50
          70
output:   55 66

#Explination: The program prints all palindrome numbers within the given range by 
              checking if each number reads the same forwards and backwards.
          ''')


def mergedictionaries():
    print("\n10. Merge Dictionaries")
    print('''
dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

merged = {**dict1, **dict2}

print("Merged dictionary:", merged)
          
#Example 1:
input:  Enter first dictionary: {'a': 1, 'b': 2}
        Enter second dictionary: {'c': 3, 'd': 4}
output: Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Example 2:
input:  Enter first dictionary: {'x': 10, 'y': 20}
        Enter second dictionary: {'y': 99, 'z': 30}
output: Merged dictionary: {'x': 10, 'y': 99, 'z': 30}

#Explination: This code merges two dictionaries into one, 
              with values from the second dictionary overriding duplicates from the first.
''')
