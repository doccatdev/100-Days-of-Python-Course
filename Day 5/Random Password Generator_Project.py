#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in letters:
    i = (random.choices(letters, k = nr_letters))
    for x in symbols:
        x = (random.choices(symbols, k = nr_symbols))
        for y in numbers:
            y = (random.choices(numbers, k = nr_numbers))
            

print(f'Random Letters List generated: {i}')
print(f'Random Symbols List generated: {x}')
print(f'Random Numbers List generated: {y}')

combine_of_list_easy = ''.join(i) + ''.join(x) + ''.join(y)
print(f'Your Easy Level Mode Password is: {combine_of_list_easy}')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Loop for each list 
for i in letters:
    i = (random.choices(letters, k = nr_letters))
    for x in symbols:
        x = (random.choices(symbols, k = nr_symbols))
        for y in numbers:
            y = (random.choices(numbers, k = nr_numbers))
            
#print all random list from letters, symbols, and numbers
print(f'Random Letters List generated: {i}')
print(f'Random Symbols List generated: {x}')
print(f'Random Numbers List generated: {y}')

#randomize all list (i= letters, x = symbols, y = numbers)
random.shuffle(i)
random.shuffle(x)
random.shuffle(y)

#Join all list to generate new password
combine_of_list_hard = ''.join(i) + ''.join(x) + ''.join(y)

#Output
print(f'Your Hard Level Mode Password is: {combine_of_list_hard}')

