import os
from art import logo
clear = lambda: os.system("clear")
all_bids = {}
bidding_ended = False
print(logo)

def find_winning_bidder(all_bids):
    highest_bid = 0
    winner = ""        
    for bidder in all_bids:
        bid_amount = all_bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bid was {highest_bid} and the winner is {winner}.")

# pokus
while not bidding_ended:
    name = input("What is your name? ")
    price = int(input("What is your bid: $"))
    all_bids[name] = price
    continue_bidding = input("Are there any more bidders? Type 'yes' or 'no':\n")
    if continue_bidding == "no":
        bidding_ended = True
    clear()
    
find_winning_bidder(all_bids)



