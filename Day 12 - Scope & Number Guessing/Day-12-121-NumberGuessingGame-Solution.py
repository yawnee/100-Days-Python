from random import randint
from art import logo

# Global Constant
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

print(logo)

# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty
def set_difficulty():
    level = input("Chosoe a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 10.
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")  # De bugging

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        # Track the number of turns and reduce by 1 if they get it wrong
        if turns == 0:
            print("You've run out of guesses, you lose!")
            return  # Return exists the code
        elif guess != answer:
            print("Guess again!")

game()
