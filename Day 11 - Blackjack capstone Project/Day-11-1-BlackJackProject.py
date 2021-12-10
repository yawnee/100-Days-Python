############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
from typing import Dict

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo


def deal_card():
    """
    :return: a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(cards):
    """
    :param cards: Take a list of cards and calculate the cards
    :return:
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, the dealer has blackjack!"
    elif user_score == 0:
        return "Wins, has a blackjack!"
    elif user_score > 21:
        return "Lose, bust!"
    elif computer_score > 21:
        return "Win, dealer bust!"
    elif user_score > computer_score:
        return "Win, you have a higher number!"
    else:
        return "You lose"

print(calculate_score(user_cards))
print(calculate_score(computer_cards))
print(user_cards)
print(computer_cards)
while is_game_over is False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over is True
        print("you lose!")
    else:
        user_should_deal = input("Do you want to draw another card? ") == 'y'
        if user_should_deal == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            is_game_over is True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))
