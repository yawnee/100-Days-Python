# Recommended tools:
# Pycharm debugging feature
# Thorny
# https://pythontutor.com/visualize.html#mode=edit

############DEBUGGING#####################
# Uncomment each block one by one and understand the bug

# Describe Problem
# No 21 in the range to be "20"
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# Make randint(6,6), as this index is out of range
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  # Needs to be (0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year 1994 becomes equal which the if statement does not have
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:  # Put >=
#   print("You are a Gen Z.")

# # Fix the Errors
# If statement needs block and input should have int() instead of str to compare and include F string in age
# age = input("How old are you?")
# if age > 18:  # Needs indented block
# print("You can drive at age {age}.")  # needs f string

# #Print is Your Friend
# Remove the extra = in word_per_page
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))  # remove the extra =
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# The b_list is outside of the for loop, it should be in
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)  # the list should be within the for loop
#   print(b_list)
#
# mutate([1,2,3,5,8,13])