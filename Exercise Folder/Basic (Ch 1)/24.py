One_Day = 86400
One_Hours = 3600
One_Minutes = 60
One_Second = 1

X = int(input("Write Total Days : "))

Y = int(input("Write Total Hours : "))

Z = int(input("Write Total Minutes : "))

W = int(input("Write Total Second : "))

Day_Time = One_Day * X
Hour_Time = One_Hours * Y
Minute_Time = One_Minutes * Z
Second_Time = One_Second * W
Times = Day_Time + Hour_Time + Minute_Time + Second_Time
print(f"DD:{Day_Time} HH:{Hour_Time} MM:{Minute_Time} SS:{Second_Time}")
print(f"The total number of seconds is: {Times} seconds")
