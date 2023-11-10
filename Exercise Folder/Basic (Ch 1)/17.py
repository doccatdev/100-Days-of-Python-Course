# Exercise 17 : Heat Capacity

# Heat mass of water in joule
C = 4.186
# Example value of electrical price
ELECTRICAL_PRICE = 8.9
# 2.777e7 = 2.777 * 10^-7
J_to_KWH = 2.777e7

m = input("Enter the mass value : ")
# change in temperature
t2 = int(input("Change temprature value 2 : "))
t1 = int(input("Change temprature value 1 : "))
# Delta T (change in temperature )
t3 = t2 - t1
# mass value
m = float(m)

q = m * C * t3

print(f"That will require,{q} Joules of energy.")

# Compute the cost
kwh = q * J_to_KWH
cost = kwh * ELECTRICAL_PRICE

# Display the cost
print("That much energy will cost %.2f cents." % cost)
