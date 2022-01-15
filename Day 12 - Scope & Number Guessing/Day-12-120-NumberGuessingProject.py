# Introducing the final project: the number guessing game

import random
from art import logo

print(logo)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type ' easy' or 'hard': ")
difficulty.lower()

while not difficulty == ('easy' or 'hard'):
    difficulty = input(f"Error, not the correct answer. Please insert answer: ")
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
print("")

randomNumber = random.randint(1, 100)
is_game_over = False
betweenNumber = False


def compare(answer, randomNumber):
    if answer < randomNumber:
        return "Too low. \nGuess again!\n"
    elif answer > randomNumber:
        return "Too high \nGuess again!\n"
    else:
        return "You lose"


print(f"You have {lives} attempts remaining to guess the number!")
answer = int(input("Make a guess: "))
print("")
while not betweenNumber:
    if answer > 100 or answer < 0:
        answer = int(input("Please insert a number between 1 to 100: "))
    else:
        betweenNumber = True

print(f"Debugging help!!: Answer: {answer}, RandomNumber: {randomNumber}")

while not is_game_over:
    print(compare(answer, randomNumber))
    answer = int(input("Make a guess: "))
    if answer == randomNumber:
        print(f"You won! You had {lives} lives remaining!")
        is_game_over = True
    else:
        lives -= 1
        if lives == 0:
            print("You ran out of lives!")
            is_game_over = True
        elif lives != 0:
            print(f"You have {lives} lives remaining!")
