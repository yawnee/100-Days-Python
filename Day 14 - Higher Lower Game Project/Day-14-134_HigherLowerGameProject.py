from game_data import data
from art import logo, vs
import random

print(logo)


def game():
    game_over = False
    score = 0
    while not game_over:
        random_number1 = random.randint(0, 49)
        random_number2 = random.randint(0, 49)
        while random_number1 == random_number2:
            random_number2 = random.randint(0, 49)

            #  Follower 1 ---------
            #  print(data[random_number1])
            follower1 = data[random_number1]
            print(f'Compare A: ' + (follower1['name']) + ', a ' + (follower1['description']) + ', from ' + (
            follower1['country']))
            print(follower1['follower_count'])
            follower1_count = int((follower1['follower_count']))  # Debug help

            #  -----
            print(vs)

            #  Follower 2 -------------
            #  print(data[random_number2])
            follower2 = data[random_number2]
            print(f'Compare B: ' + (follower2['name']) + ', a ' + (follower2['description']) + ', from ' + (
            follower2['country']))
            print(follower2['follower_count'])
            follower2_count = int((follower2['follower_count']))  # Debug help

            guess = input("Who has more followers? Type 'A' or 'B': ")
            guess = guess.lower()
            # check_answer(guess, follower1_count, follower2_count, score)
            if guess == 'a':
                if follower1_count > follower2_count:
                    score += 1
                elif follower1_count < follower2_count:
                    game_over = True
            elif guess == 'b':
                if follower2_count > follower1_count:
                    score += 1
                elif follower2_count < follower1_count:
                    game_over = True

    print(f'Your final score is: {score}')


game()


# Self thinking steps to do:
# Steps to do

# Step 1: print(logo)

# Step 2: Compare A: Random on list

# Step 3: print(vs)

# Step 4: against B: Random on list

# Step 5: Who has more followers? Type A or B

# Step 6: Compare program

# Step 6.1: If right, give score and compare with a new competitor

# Step 6.1: If wrong, give final score and end the game
