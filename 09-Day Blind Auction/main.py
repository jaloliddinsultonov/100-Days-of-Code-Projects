from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


def bidder_adder(bidder, amount):
    bidders[bidder] = amount


print(logo)
bidders = {}
print("Welcome to the secret auction program.")
choice = True
while choice:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidder_adder(bidder=name, amount=bid)
    answer = input("Are there any other bidders? Type \"yes\" or \"no\".\n")
    if answer == 'no':
        choice = False
        break
    else:
        choice = True
        clear()

prices_list = []
for person in bidders:
    prices_list.append(bidders[person])

max_price = max(prices_list)

highest_value = 0
for person in bidders:
    price = bidders[person]
    if price > highest_value:
        highest_value = price
        winner = person
print(f"The winner is {winner} with a bid of ${max_price}")