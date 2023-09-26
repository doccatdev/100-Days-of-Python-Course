#Create greeting for your program
print("Welcome to Tip Calculator")
#Ask user input like bills, people, and tip
bills = input("What was total bill ? $")
people = input("How many people to split the bill ? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15 ? ")

#Create new variable called new_bills to Convert str to float for bills variable in input function
new_bills = float(bills)
#Create new variable called new_people to Convert str to int for people variable in input function
new_people = int(people)
#Create new variable called new_people to Convert str to int for tip variable in input function
new_tip = int(tip)

#Tip percent = tip divide by 100
tip_percent = new_tip / 100
#Total tip = bills mulitply by tip percent
total_tip = new_bills * tip_percent
#Total bills = bils addition by tip
total_bills = new_bills + total_tip
#Bill per person = total bills divide people
bill_person = total_bills / new_people

#Total amount round to 2 decimal
total_amount = "{:.2f}".format(bill_person)

#Output program
print(f"Each person should pay ${total_amount}")
