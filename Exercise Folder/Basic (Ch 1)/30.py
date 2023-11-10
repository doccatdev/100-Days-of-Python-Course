# Exercise 30 : Celcius to Fahrenheit and Kelvin
temp = input("Temperature (in celcius degree) : ")

temp = float(temp)

Celcius_to_Kelvin = temp + 273.15
Celcius_to_Fahrenheit = temp * (9 / 5) + 32

print(f"Temperature is (in celcius degree) : {temp} ℃")
print(f"Temperature is {Celcius_to_Kelvin} K")
print(f"Temperature is {Celcius_to_Fahrenheit} °F")
