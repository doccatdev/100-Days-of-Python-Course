import artproject

def addition(a, b):
    "Take number a and b then return the addition a and b"
    return a + b

def subtract(a, b):
    "Take number a and b then return the substract a and b"
    return a - b

def multiply(a, b):
    "Take number a and b then return the multiply a and b"
    return a * b

def division(a, b):
    "Take number a and b then retrun the division a and b"
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculator():
    "Take number num1 and num2 then doing calculator operation based on user option"
    while True:
        print(artproject.ascii_art)
        num1 = float(input("What's the first number: "))
        while True:
            operation_symbol = ["+","-","*","/"]
            for x in operation_symbol:
                print(x)
            user_choise = input("Pick on Operation: ")
            num2 = float(input("What's the next number: "))
            if user_choise == "+":
                result = addition(num1,num2)
            elif user_choise == "-":
                result = subtract(num1,num2)
            elif user_choise == "*":
                result = multiply(num1, num2)
            elif user_choise == "/":
                result = division(num1, num2)
            else:
                print("Error: Option does not exist")
                continue
            print(f"Result: {num1} {user_choise} {num2} = {result}")

            restart = input(f"Type 'y' to continue with this result {result}, or 'n' to start a new calculation: ")
            if restart == 'y':
                num1 = result
            else:
                print("\n"*5)
                break
calculator()