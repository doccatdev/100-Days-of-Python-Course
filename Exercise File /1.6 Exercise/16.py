# Exercise 16 : Area and Volume of Circle

import math

pi = math.radians(180)

r = input("Input the radius value : ")

r = float(r)

area = pi * r**2
volume = 4 / 3 * pi * r**3

print("Area of Circle : ", area)
print("Volume of Circle : ", volume)
