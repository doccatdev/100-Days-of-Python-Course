# Exercise 10 : Arithmetic

# Import math library to call log10 function
from math import log10

# Give user input from keyboard
x = input("Type first number  : ")
y = input("Type second number : ")

# Type conversion
x = int(x)
y = int(y)

# Calculate the x and y value and display output
print(x, "+", y, "is", x + y)
print(x, "-", y, "is", x - y)
print(x, "*", y, "is", x * y)
print(x, "/", y, "is", x / y)
print("The base 10 logarithm of", x, "is", log10(x))
print(x, "x^y", y, "is", x**y)