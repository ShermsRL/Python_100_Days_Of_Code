# Day 5 Lesson---------------------------------------------------------------------------------------------------------
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")

# total = 0
# for number in range(1,101):
#   total += number
# print (total)

alphabet = ["a", "b", "c"]
for char in alphabet:
  print(char)

# Day 5 Challenge------------------------------------------------------------------------------------------------------
# Password Generator Project
import random


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_password = []
for letter in range(1, nr_letters + 1):
    ran_let = random.choice(letters)
    random_password.append(ran_let)

for number in range(1, nr_symbols + 1):
    ran_symb = random.choice(symbols)
    random_password.append(ran_symb)

for symbol in range(1, nr_numbers + 1):
    ran_num = random.choice(numbers)
    random_password.append(ran_num)

random.shuffle(random_password)
print("Your Password is: " + ''.join(random_password))
