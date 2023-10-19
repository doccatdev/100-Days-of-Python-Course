#Exercise 4 : Area of a Field

#Value that convert from square feet to acre
SQFT_PER_ACRE = 43560

#Length user input
length = input("Lenth of Area ?")

#Width user input
width = input("Width of Area ?")

#Type conversion from string to float number
length_cov = float(length)
width_cov = float(width)

#Calculate total area in acre
total_area = length_cov * width_cov / SQFT_PER_ACRE

#Print the calculation result
output = print(f"There are {total_area} square feet in an acres")