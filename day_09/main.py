# Secret Auction
from art import logo
bids = {}
taking_bids = True
print(logo)
print("Welcome to the Secret Auction program")
while taking_bids:
    name = input("What is your name?\n>> ")
    bid = int(input("what is your bid?\n>> £"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n>> ")
    if more_bidders == 'no':
        taking_bids = False
    else:
        print("\n" * 20)

highest_bid = 0
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of £{highest_bid}")
