# Exercise 6 : Tax & Tip

# User cost input
meal_cost = input("Cost of a meal?" " " "Rp.")

# Tyoe convert
meal_cost_conv = float(meal_cost)
# # In this case, I use restaurant tax
Tax & Tip Rate
Tax = 0.10
Tip = 0.18

# Tax calculation
tax = meal_cost_conv * Tax
# Tip calculation
tip = meal_cost_conv * Tip

# Total bill calculation (Tip, Tax and Food cost)
total_bill = tip + tax + meal_cost_conv
output = "The tax is Rp.%.2f and the tip is Rp.%.2f, making the total Rp.%.2f" % (
     tax,
     tip,
     total_bill,
 )

# Display output
print(output)