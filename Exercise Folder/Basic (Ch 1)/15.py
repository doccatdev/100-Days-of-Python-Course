# Exercise 15 : Distance Unit


x = input("Enter in feet : ")
x = float(x)

yard_value = 3
inches_value = 12
miles_value = 5.280

yard = x / yard_value

inches = x * inches_value

miles = x * miles_value

print("Feet to inches", ": ", inches)
print("Feet to yard", ": ", yard)
print("Feet to miles", ": ", miles)
