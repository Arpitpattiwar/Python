from art import logo

run_calc = True


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1/num2

print(logo)

while run_calc:
    operator = input("Which operation do you want to perform. +, -, *, /:\n")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(add(num1, num2))

    elif operator == "-":
        print(subtract(num1, num2))

    elif operator == "*":
        print(multiply(num1, num2))

    elif operator == "/":
        print(divide(num1, num2))

    else:
        print("Incorrect input")

    if input("Do you want to continue: ").lower() != "yes":
        run_calc = False
