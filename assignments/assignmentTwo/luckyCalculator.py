# Riley Ahlrichs                2-19-2025
# Assignment 2

# This is my calculator program that allows the user to choose between 7 operations or pick their lucky
# number. If they don't choose one of the 3 options, the program will say to choose from the 3 provided.

import random

print("Lucky Calculator\n")
print("By: Riley Ahlrichs")
print("{COMS 1270 Section 1}\n")

print("Please choose what you'd like to do!\n")
choice = input("[c]alculator, [l]ucky number, [q]uit: ")
print("----------------------------------------------")
if choice == 'c':
    operation = input("Please choose an operation [+], [-], [*], [/], [//], [%], [**]: ")

    if operation == '+':       # Addition
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        answer = num1 + num2
        print(f"The answer to {num1} + {num2} is: {answer}")

    elif operation == '-':     # Subtraction
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        answer = num1 - num2
        print(f"The answer to {num1} - {num2} is: {answer}")

    elif operation == '*':     # Multiplication
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        answer = num1 * num2
        print(f"The answer to {num1} * {num2} is: {answer}")

    elif operation == '/':     # Division
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        if num2 == 0:
            print("Error, cannot divide by 0. Denominator will change to 1.")
            num2 = 1
        answer = num1 / num2
        print(f"The answer to {num1} / {num2} is: {answer}")

    elif operation == '//':     # Floor Division
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        if num2 == 0:
            print("Error, cannot floor divide by 0. Denominator will change to 1.")
            num2 = 1
        answer = num1 // num2
        print(f"The answer to {num1} // {num2} is: {answer}")

    elif operation == '%':     # Modulus
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        if num2 == 0:
            print("Error, cannot calculate modulus with 0. Your second number will change to 1.")
            num2 = 1
        answer = num1 % num2
        print(f"The answer to {num1} % {num2} is: {answer}")

    elif operation == '**':     # Exponent
        num1 = int(input("Enter the base integer: "))
        num2 = int(input("Enter the exponent integer: "))
        answer = num1 ** num2
        print(f"The answer to {num1} ** {num2} is: {answer}")

    else:
        print("Invalid operation: try agian!")

elif choice == 'l':     # Lucky Number
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    lucky_number = random.randrange(num1, num2)
    print(f"This is your lucky number!: {lucky_number}")

elif choice == 'q':
    print("Goodbye!")
else:
    print("Invalid choice: Please choose from [c], [l], or [q].")
