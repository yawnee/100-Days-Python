#Understanding offset and appending items to lists
#example; fruits = [item1,item2]
#Data structure lists

states_of_america = ["Deleaware", "Pennsylvania", "New York"]

print(states_of_america[0])
states_of_america[-1] = "new bisahsa"
print(states_of_america[-1])

states_of_america.append("Yawnee_Land")

print(states_of_america)

#Code challenge below#############
#################################

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

print(names)
list_length = int(len(names) - 1)

random_person = random.randint(0,list_length)
print(f"Your are paying, {names[random_person]}!")

# You can simply do this

random_person = random.choice(names)

