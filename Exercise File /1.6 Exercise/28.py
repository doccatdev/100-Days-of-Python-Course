user_height = input("Give the user height (in inches) : ")
user_weight = input("Give the user weight (in pound) : ")

user_height = float(user_height)
user_weight = float(user_weight)

bmi = (user_weight) / (user_height * user_height) * 703
format_bmi = "{:.0f}".format(bmi)
print(f"Your Body Mass Index is {format_bmi} kg/m^2")
