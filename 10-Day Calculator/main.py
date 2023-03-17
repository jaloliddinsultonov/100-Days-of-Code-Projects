from replit import clear
from art import logo

#Calculator


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiple
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    answer = num1
    while True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        for symbol in operations:
            if symbol == operation_symbol:
                process = operations[symbol]
                answer2 = process(answer, num2)

        print(f"{answer} {operation_symbol} {num2} = {answer2}")
        answer = answer2
        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: "
        )
        if choice == "y":
            continue
        elif choice == "n":
            clear()
            calculator()
            break
        else:
            print("Wrong input.")


calculator()
