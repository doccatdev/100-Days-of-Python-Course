#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Random Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Input validation and generation of letters
if nr_letters < 1 or nr_letters > 52:
    print('Your Letters input is out of range. It must be between 1 and 52.')
    i = []  # Empty list if input is invalid
    exit()
else:
    i = []  # Initialize list for letters
    for char in range(1, nr_letters + 1):
        i.append(random.choice(letters))  # Add one random letter per loop

# Input validation and generation of symbols
if nr_symbols < 1 or nr_symbols > 10:
    print('Your Symbols input is out of range. It must be between 1 and 10.')
    x = []  # Empty list if input is invalid
    exit()
else:
    x = []  # Initialize list for symbols
    for char in range(1, nr_symbols + 1):
        x.append(random.choice(symbols))  # Add one random symbol per loop

# Input validation and generation of numbers
if nr_numbers < 1 or nr_numbers > 10:
    print('Your Numbers input is out of range. It must be between 1 and 10.')
    y = []  # Empty list if input is invalid
    exit()
else:
    y = []  # Initialize list for numbers
    for char in range(1, nr_numbers + 1):
        y.append(random.choice(numbers))  # Add one random number per loop
            

print(f'Random Letters generated: {i}')
print(f'Random Symbols generated: {x}')
print(f'Random Numbers generated: {y}')

combine_of_list = ''.join(i) + ''.join(x) + ''.join(y)
print('Easy Level Mode')
print(f'Your Arranged (Order) Generated Password is: {combine_of_list}')

###############################################################################################################################################################################

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Loop for each list 
# Password Generator Project
# Get user input
nr_letters = int(input("How many letters would you like in your password? (1-52)\n"))
nr_symbols = int(input("How many symbols would you like? (1-10)\n"))
nr_numbers = int(input("How many numbers would you like? (1-10)\n"))

# Input validation and generation of letters
if nr_letters < 1 or nr_letters > 52:
    print('Your Letters input is out of range. It must be between 1 and 52.')
    i = []  # Empty list if input is invalid
    exit()
else:
    i = []  # Initialize list for letters
    for char in range(1, nr_letters + 1):
        i.append(random.choice(letters))  # Add one random letter per loop

# Input validation and generation of symbols
if nr_symbols < 1 or nr_symbols > 10:
    print('Your Symbols input is out of range. It must be between 1 and 10.')
    x = []  # Empty list if input is invalid
    exit()
else:
    x = []  # Initialize list for symbols
    for char in range(1, nr_symbols + 1):
        x.append(random.choice(symbols))  # Add one random symbol per loop

# Input validation and generation of numbers
if nr_numbers < 1 or nr_numbers > 10:
    print('Your Numbers input is out of range. It must be between 1 and 10.')
    y = []  # Empty list if input is invalid
    exit()
else:
    y = []  # Initialize list for numbers
    for char in range(1, nr_numbers + 1):
        y.append(random.choice(numbers))  # Add one random number per loop

# Print all random lists
print(f'Random Letters generated: {i}')
print(f'Random Symbols generated: {x}')
print(f'Random Numbers generated: {y}')

# Randomize all lists
random.shuffle(i)
random.shuffle(x)
random.shuffle(y)

# Combine all lists to generate the password
combine_of_list = ''.join(i) + ''.join(x) + ''.join(y)

# Output password
print('Hard Level Mode')
print(f'Your Randomized Generated Password is: {combine_of_list}')
