import random
word_list = ["sonic", "red", "haruki", "resident", "evil", "doom", "spyro", "halo"]

#TODO-1 - Randomly choose a word from the list and assign it to a variable called chosen_word

num_of_words = (len(word_list))

print(num_of_words)
chosen_word = word_list[random.randint(0, num_of_words -1)]
print(chosen_word)

for letter in chosen_word:
    print(end="_")
print("\n")

each_letter = [ ]

for letter in chosen_word:
    print(letter)
    each_letter.append(letter)
print("\n")

print(each_letter)

# My Terrible attempt below, semi correct still works
hidden_letter = []
length = int(len(chosen_word))
b = 0
while not length == b:
    b += 1
    hidden_letter.append("_")
print(hidden_letter)

# EASIER SOLUTION 1st solution
display = []
for letter in chosen_word:
    display += "_"
print(display)

# # EASIER SOLUTION 2nd solution
# for _ in range(len(chosen_word)):
#     display += "_"
# print(display)



#TODO-2 - ASk the user to guess a letter and assign their answer to a variable called guess. Make guess lower case

guess = input("Guess a letter: ").lower()


#TODO-3 - Check letter guessed is one of the letters in the chosen word


# My solution below
x = 0
for letter in chosen_word:
    if guess == letter:
        #print(f"{letter}")
        #print("Correct")
        hidden_letter.pop(x)
        hidden_letter.insert(x, letter)
    #else:
        #print("Wrong")
    x += 1

# EASIER Tutorial Solution
for position in range(len(chosen_word)):
    letter1 = chosen_word[position]
    if letter1 == guess:
        display[position] = letter1


#TODO-4: Create an empty list called display
# For each letter in the chosen_word add a _ to display

print(hidden_letter)
print(display)
# hidden_letter = []
# length = int(len(chosen_word))
# b = 0
#
# while not length == b:
#     b += 1
#     hidden_letter.append("_")
# print(hidden_letter)



length = len(chosen_word)
# for x in range(length):
#     print("_")

