# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests


n1=name1.lower()

n2=name2.lower()

t=n1.count("t") + n2.count("t")
r=n1.count("r") + n2.count("r")
u=n1.count("u") + n2.count("u")
e=n1.count("e") + n2.count("e")

sum1= t+r+u+e

l=n1.count("l") + n2.count("l")
o=n1.count("o") + n2.count("o")
v=n1.count("v") + n2.count("v")
e=n1.count("e") + n2.count("e")

sum2=l+o+v+e

score= int(str(sum1) + str(sum2))

if score<=10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score>=40 and score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")