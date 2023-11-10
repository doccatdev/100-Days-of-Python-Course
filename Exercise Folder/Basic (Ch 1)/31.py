# Exercise 31 : Unit of pressure

# Initialize 1 PSA, 1 Millimeter Mercury, 1 atm value is equal to kPa
PSA_value = 0.14503773800722
millimeter_mercury_value = 7.50062
atm_value = 0.00986923266

# User input
kilo_pascal = input("Pressure (in kilopascal) ? : ")
# Type convert
kilo_pascal = int(kilo_pascal)

# Convert KPa to PSI
kpi_to_psi = kilo_pascal * PSA_value

# Convert KPa to Millimeter Mercury
kPa_to_millimeter_mercury = kilo_pascal * millimeter_mercury_value

# Convert KPa to atm
kPa_to_atm = kilo_pascal * atm_value
print("Result : ")
print(f"{kilo_pascal} KPa is equal to {kpi_to_psi} PSI")
print(f"{kilo_pascal} KPa is equal to {kPa_to_millimeter_mercury} Millimeter Mercury")
print(f"{kilo_pascal} KPa is equal to {kPa_to_atm} atm")
