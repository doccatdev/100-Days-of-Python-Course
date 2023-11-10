# Exercise 28 : BMI Calculator

# Pounds and Inches

# user_height = input("Give the user height (in inches) : ")
# user_weight = input("Give the user weight (in pound) : ")

# user_height = float(user_height)
# user_weight = float(user_weight)

# bmi = (user_weight) / (user_height **2) * 703
# format_bmi = "{:.0f}".format(bmi)
# print(f"Your Body Mass Index is {format_bmi} kg/m^2")


# Kilograms

user_height_cm = input("Give the user height (in cm) : ")
user_weight_kg = input("Give the user weight (in kg) : ")

user_height_cm = float(user_height_cm)
user_weight_kg = int(user_weight_kg)

user_height_m = user_height_cm / 100


bmi_kg = user_weight_kg / user_height_m**2
format_bmi_kg = "{:.2f}".format(bmi_kg)
print(f"Your Body Mass Index is {format_bmi_kg} kg/m^2")
