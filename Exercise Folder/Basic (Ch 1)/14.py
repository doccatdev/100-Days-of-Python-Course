# Exercise 14 : Height Unit

IN_PER_FT = 12
CM_PER_IN = 2.54


# Read the height from the user
print("Enter your height:")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))

# # Compute the equivalent number of centimeters
cm = (feet * IN_PER_FT + inches) * CM_PER_IN

# # Display the result
print("Your height in centimeters is:", cm)
