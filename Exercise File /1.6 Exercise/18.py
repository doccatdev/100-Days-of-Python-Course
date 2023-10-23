# Exercise 18 : Volume of Cylinder

# Formula : phi * r**2 * h

import math

pi = math.radians(180)

r = input("Input the radius of cylinder : ")
h = input("Input the height of cylinder : ")

r = float(r)
h = float(h)

volume = pi * r**2 * h
volume_round = round(volume, 1)
print(f"The volume of cylinder is {volume_round}")
