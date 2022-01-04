import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_hands = [rock, paper, scissors]

player1_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
player1_input = int(player1_input)
print(f"\n{game_hands[player1_input]}")

bot1_input = random.randint(0, 2)
print(f'Computer chose: {game_hands[bot1_input]}')

if player1_input == 0 and bot1_input == 0:
    print("Draw")
elif player1_input == 0 and bot1_input == 1:
    print("You lose")
elif player1_input == 0 and bot1_input == 2:
    print("You won")
elif player1_input == 1 and bot1_input == 0:
    print("You won")
elif player1_input == 1 and bot1_input == 1:
    print("You Draw")
elif player1_input == 1 and bot1_input == 2:
    print("You lose")
elif player1_input == 2 and bot1_input == 0:
    print("You lose")
elif player1_input == 2 and bot1_input == 1:
    print("You won")
elif player1_input == 2 and bot1_input == 2:
    print("You Draw")
