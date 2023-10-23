# Exercise 19 : Free Fall

import math

g = 9.8

d = input("Height (in meters) : ")

d_float = float(d)

vf = math.sqrt(2 * g * d_float)

print("It will hit the ground at %.2f m/s." % vf)
