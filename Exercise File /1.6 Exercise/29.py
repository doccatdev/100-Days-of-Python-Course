# Exercise 29 : Wind Chill Index

wind = input("Wind speed :  ")

temp = input("Air temperature :  ")

wind = float(wind)

temp = float(temp)

wci_index = 13.12 + 0.6215 * temp - 11.37 * wind**0.16 + 0.3965 * temp * wind**0.16
formating = "{:.0f}".format(wci_index)
print(f"The wind chil index is {formating} ℃")


## This code below is solution from the book itself ##
# ##
# # Compute the wind chill index for a given air temperature and wind speed.
# #
# WC_OFFSET = 13.12
# WC_FACTOR1 = 0.6215
# WC_FACTOR2 = -11.37
# WC_FACTOR3 = 0.3965
# WC_EXPONENT = 0.16

# # Read the air temperature and wind speed from the user
# temp = float(input("Air temperature (degrees Celsius): "))
# speed = float(input("Wind speed (kilometers per hour): "))
# # Compute the wind chill index
# wci = (
#     WC_OFFSET
#     + WC_FACTOR1 * temp
#     + WC_FACTOR2 * speed**WC_EXPONENT
#     + WC_FACTOR3 * temp * speed**WC_EXPONENT
# )
# # Display the result rounded to the closest integer
# print("The wind chill index is", round(wci))
