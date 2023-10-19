#Exercise 3 : Area of Room

#Give user input
lenth = input ("Lenth of Room")
width = input("Width of Room")

#Type convertion from str to floating point numbers
l_convert = float (lenth)
w_convert = float(width)

#Calculate area l * w
area = w_convert * l_convert

#Display output
print (f"{area}", "meters")