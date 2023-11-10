# Exercise 20 : Ideal Gas Law

R = 8.314  # J / mol K

# Input pressure value
Y = input("Input the pressure : ")
Y = float(Y)
# Input volume value
Z = input("Input the volume : ")
Z = float(Z)
# Input temp value
X = input("Input the temperature : ")
X = float(X)

# Convert from celcius to kelvin
C_to_K = X + 273.15
# Convert pressure to atm
P_to_atm = Y * 0.00000986923

# Calculate amount gas
n = Y * Z / R * X
print(n)
