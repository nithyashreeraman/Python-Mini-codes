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
import random 
game_images = [rock, paper, scissors]
user=int(input("Enter(1-rock/2-paper/3-scissors):\n"))
print(game_images[user-1])

comp=random.randint(1,3)
print("Computer chose:\n")
print(game_images[comp-1])

if user>= 4 or user<=0: 
  print("You typed an invalid number, you lose!") 
elif user == 1 and comp== 3:
  print("You win!")
elif comp == 1 and user== 3:
  print("You lose")
elif comp>user:
  print("You lose")
elif user>comp:
  print("You win!")
elif comp == user:
  print("It's a draw")


