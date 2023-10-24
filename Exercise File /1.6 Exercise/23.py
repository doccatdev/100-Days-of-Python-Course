# # Exercise : Area of a Regular Polygon

from math import tan, pi

s = input("Input the length side value : ")
s = float(s)

n = input("Input number of side of Polygon : ")
n = float(n)

area = (n * s**2) / (4 * tan(pi / n))
print(f"The Area of Regular Polygon is {area} cm^2")
