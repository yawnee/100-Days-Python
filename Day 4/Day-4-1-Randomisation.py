#rock, paper, scissors - Randomism

import random

random_integer = random.randint(1, 10)
print(random_integer)

#Module (spliting up code for multiple people to work on it)
#How to create your own module

import Day_4_1_my_module
print(Day_4_1_my_module.pi)

random_float = random.randint(0,1)
if random_float == 0:
    print("You have landed on Heads!")
elif random_float == 1:
    print("you have landed on Tails!")


