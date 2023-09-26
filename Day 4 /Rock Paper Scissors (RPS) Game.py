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

#Write your code below this line 👇
import random

rps_list = [rock, paper, scissors]

user_input = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if user_input >= 3 or user_input < 0:
  print("You type wrong number, game over!")
else:
  print(rps_list[user_input])
  
  random_computer = random.randint(0,2)
  print("Computer choose")
  print(rps_list[random_computer])
  
  if user_input == 0 and random_computer == 2:
    print("You win")
  elif random_computer == 0 and user_input == 2:
    print("You lose")
  elif random_computer > user_input:
    print("You lose")
  elif user_input > random_computer:
    print("You win")
  elif random_computer == user_input:
    print("Draw")
  
