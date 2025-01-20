# Rock Paper Scissors ASCII Art
print('Welcome to Rock Paper Scissors Game')
print('What do you want to choise? Type 0 for Rock, 1 for Paper, 2 for Scissors')
input_user = int(input('Your choise: '))
if input_user < 0 or input_user > 2:
    print('You chose an invalid option. Please try again!')
    exit()
user_name = input('Enter Your Name:')


ascii_art = [
    # Rock
    """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    
    # Paper
    """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    
    # Scissors
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
]


if input_user == 0:
    print(ascii_art[0])
elif input_user == 1:
    print(ascii_art[1])
elif input_user == 2:
    print(ascii_art[2])

import random
computer = random.randrange(0,2)
print ('The Computer Choise is:')
print(ascii_art[computer])

if input_user == 0 and computer == 2:
    print(f'{user_name} Win')
elif computer == 0 and input_user == 2:
    print(f'{user_name} Lose')
elif computer > input_user:
    print(f'{user_name} Lose')
elif input_user > computer:
    print(f'{user_name} Win')
elif input_user == computer:
    print('Draw')




