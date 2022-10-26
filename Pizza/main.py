# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
if size=='S':
  bill=15
  if add_pepperoni=='Y':
    bill+=2

elif size=='M':
  bill=20
  if add_pepperoni=='Y':
    bill+=3
else:
  bill=25
  if add_pepperoni=='Y':
    bill+=3

if extra_cheese=='Y':
  bill+=1

print(f"Your final bill is: ${bill}.")