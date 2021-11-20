#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for x in letters.split(,):
#     letters = int(letters)
#
# nr_letters = int(nr_letters)
# print(nr_letters)
#
# Random_Number = letters.randint(0, 20)
# print(Random_Number)
# Random_Number = int(Random_Number)

len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)
int_letters = int(nr_letters)
int_symbols = int(nr_symbols)
int_numbers = int(nr_numbers)

PASSWORD = []
FINAL_PASSWORD = []
#states_of_america.append("Yawnee_Land")

lenth_of_password = int_numbers + int_symbols + int_letters

for a in range(0, int_letters):
    add_character = random.randint(0, len_letters - 1)
    #print(add_character)
    PASSWORD.append(letters[add_character])
    #print(letters[add_character]) #to show case it works
    #print(PASSWORD) #to show case password is growing

#print(f"This is the final password {PASSWORD}")

for b in range(0, nr_symbols):
    add_character = random.randint(0, len_symbols - 1)
    PASSWORD.append(symbols[add_character])
    #print(symbols[add_character]) #to show case it works
    #print(PASSWORD) #to show case password is growing

#print(f"This is the final password {PASSWORD}")

for c in range(0, nr_numbers):
    add_character = random.randint(0, len_numbers - 1)
    PASSWORD.append(numbers[add_character])
    #print(numbers[add_character]) #to show case it works
    #print(PASSWORD) #to show case password is growing

print(f"This is the final password {PASSWORD}")



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for z in PASSWORD:
    add_character = random.randint(0, lenth_of_password - 1)
    # print(add_character)
    FINAL_PASSWORD.append(PASSWORD[add_character])

print(f"This is the final1 password {FINAL_PASSWORD}")


#############################################
###############################################
###################################################
# Below is the correct way to do the program

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
