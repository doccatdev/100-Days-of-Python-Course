# Exercise 8 : Widget and Gizmos

Widget_weighs = 75
Gizmos_weighs = 112

a, b = input("Enter Widget & Gizmos weight value: ").split()
print("Your Widget Weight Value : ", a)
print("Your Gizmoz Weight Value: ", b)

a = int(a)
b = int(b)

total_weighs = (75 * a) + (112 * b)
output = (
     "The Widget weighs is .%.0f grams and the Gizmos weight is %.0f grams, making the total weight is %.0f grams"
     % (a, b, total_weighs)
 )

# # Display output
print(output)