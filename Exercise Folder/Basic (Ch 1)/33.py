x = int(input("Enter the first number  : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number  : "))

min_value = min(x,y,z)
max_value = max(x,y,z)
mid_value = x + y + z - min_value - max_value

print("The numbers in sorted order are:")
print(" ", min_value)
print(" ", mid_value)
print(" ", max_value)