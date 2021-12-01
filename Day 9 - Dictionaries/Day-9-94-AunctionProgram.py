from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)

aunctioners = {}
print("Welcome to the secret aunction program.")

# def add_bidder(person, bid):
#     new_bidder = {}
#     new_bidder["Name"] = name_of_bidder
#     new_bidder["Bid"] = number_of_bid
#     aunctioners.append(new_bidder)

def find_highest_bidder(bidding_record):
    #{"Name: 123, "James": 321}
    highest_bid = 0
    winner = ""
    for bidder in aunctioners:
        bid_amount = aunctioners[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

should_continue = True
while should_continue:
    name_of_bidder = input("What is your name? \n")
    number_of_bid = int(input("What is your bid? \n"))
    answer = input("Are there any other bidders? Type 'yes' or 'no'.")

    aunctioners[name_of_bidder] = number_of_bid
    print(f"{aunctioners}\n")

    if answer == "no":
        should_continue = False
        find_highest_bidder(aunctioners)
    else:
        clear()


#solution below. My work above^:

# from replit import clear
# from art import logo
#
# print(logo)
#
# bids = {}
# bidding_finished = False
#
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     # bidding_record = {"Angela": 123, "James": 321}
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
#
# while not bidding_finished:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         clear()
#
# """
# FAQ: My console doesn't clear()
#
# This will happen if you’re using an IDE other than replit.
# I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so:
#
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076
#
# """

