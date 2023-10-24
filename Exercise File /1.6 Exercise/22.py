import math

s = input("Input the side of triangle (s) : ")
s = float(s)

s1 = input("Input lengths side of triangle (s1) : ")
s1 = float(s1)

s2 = input("Input lengths side of triangle (s2) : ")
s2 = float(s2)

s3 = input("Input lengths side of triangle (s3) : ")
s3 = float(s3)

area = s * (s - s1) * (s - s2) * (s - s3)
if area > 0:
    s = math.sqrt(area)
    print("a+b+c =", s1, s2, s3)
    print("Area =", s)
else:
    print("Please enter 3 valid sides")

# Reference : https://en.wikipedia.org/wiki/Heron%27s_formula
# Thanks to this questions for help me to fix the error in my code
# https://stackoverflow.com/questions/29375970/why-does-math-sqrt-result-in-valueerror-math-domain-error
