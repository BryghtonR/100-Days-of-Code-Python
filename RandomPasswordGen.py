#Password Generator Project

#import
import random

#selection section
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#imput section
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#password handling
password = []
password_final = []
password_str = ""

#initial random character selection
for char in range(0,nr_letters):
  password.append(random.choice(letters))
for char in range(0,nr_symbols):
  password.append(random.choice(symbols))
for char in range(0,nr_numbers):
  password.append(random.choice(numbers))

#password shuffling
for char in range(0,len(password)):
  move_index = random.randint(0,len(password)-1)
  password_final.append(password[move_index])
  password.pop(move_index)

#convert final password list to string
for char in password_final:
  password_str += char
  
print(password_str)