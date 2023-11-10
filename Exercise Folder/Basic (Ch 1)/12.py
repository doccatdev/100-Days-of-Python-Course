# Exercise 12 : Distance Between Two Points on Earth


import math

print("Distance Between Two Points on Earth")

# # Latitude
t1 = float(input("Give input for t1 : "))
t1 = math.radians(t1)

g1 = float(input("Give input for g1 : "))
g1 = math.radians(g1)

# # Longitude
t2 = float(input("Give input for t2 : "))
t2 = math.radians(t2)

g2 = float(input("Give input for g2 : "))
g2 = math.radians(g2)

# #Dilatation
dlat = t2 - t1
dlon = g2 - g1

# formula to calculate distance between two point of earth
a = math.sin(dlat / 2) ** 2 + math.cos(t1) * math.cos(t2) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = 6371.01 * c
print("The distance between the two points is {:.2f} kilometers.".format(distance))