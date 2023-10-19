#Exercise 5 : Bottle Deposits

#Compute the refund amount for a collection of bottles
LESS_DEPOSITE = 0.10
MORE_DEPOSITE = 0.25

# Read the number of containers of each size from the user
less = input("How many containers 1 litre or less?" " ")
more = input("How many containers more that 1 litre?" " ")

# Type conversion
less_int = int(less)
more_int = int(more)

# Calculate refund amount
refund = LESS_DEPOSITE * less_int + MORE_DEPOSITE * more_int

# Display output
print("Your total refund will be $%.2f." % refund)

#Exercise 6 : Tax & Tip

#User cost input
meal_cost = input("Cost of a meal?" " " "Rp.")

#Type convert
meal_cost_conv = float(meal_cost)
# In this case, I use restaurant tax
#Tax & Tip Rate
Tax = 0.10
Tip = 0.18

#Tax calculation
tax = meal_cost_conv * Tax
#Tip calculation
tip = meal_cost_conv * Tip

#Total bill calculation (Tip, Tax and Food cost)
total_bill = tip + tax + meal_cost_conv
output = "The tax is Rp.%.2f and the tip is Rp.%.2f, making the total Rp.%.2f" % (
    tax,
    tip,
    total_bill,
)

#Display output
print(output)