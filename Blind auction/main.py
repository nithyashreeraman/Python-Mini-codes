from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
bids={}

bidding=False
print("Welcome to secret auction\n")

print(logo)
while not bidding:
  name=input("What is your name:")
  cost=int(input("What is your bid:$"))
  bids[name]=cost
  ask=input("Are there any other bidders? Type 'yes or 'no'")
  if ask=="no":
    bidding=True
  elif ask=="yes":
    clear()


high=0
for i in bids:
  amount=bids[i]
  if amount>high:
    high=amount
    winner=i
print(f"\nThe winner is {winner} and the bid amount is ${high}")    
