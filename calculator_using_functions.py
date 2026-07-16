# Project Name : Calculator Using Functions
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : A simple calculator program using functions.
#                It performs Addition, Subtraction,
#                Multiplication, and Division.

# Function for Addition
def addition(a, b):
    # Return the sum of two numbers
    return a + b

# Function for Subtraction
def subtraction(a, b):
    # Return the difference of two numbers
    return a - b

# Function for Multiplication
def multiplication(a, b):
    # Return the product of two numbers
    return a * b

# Function for Division
def division(a, b):
    # Return the division of two numbers
    return a / b


# Display Calculator Menu
print("========== CALCULATOR ==========")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


# Take user's choice
choice = int(input("Enter your choice: "))

# Option 1 : Addition
if choice == 1:

    # Take first number
    num1 = int(input("Enter first number: "))

    # Take second number
    num2 = int(input("Enter second number: "))

    # Call addition function and print the result
    print("Answer =", addition(num1, num2))

# Option 2 : Subtraction
elif choice == 2:

    # Take first number
    num1 = int(input("Enter first number: "))

    # Take second number
    num2 = int(input("Enter second number: "))

    # Call subtraction function and print the result
    print("Answer =", subtraction(num1, num2))

# Option 3 : Multiplication
elif choice == 3:

    # Take first number
    num1 = int(input("Enter first number: "))

    # Take second number
    num2 = int(input("Enter second number: "))

    # Call multiplication function and print the result
    print("Answer =", multiplication(num1, num2))

# Option 4 : Division
elif choice == 4:

    # Take first number
    num1 = int(input("Enter first number: "))

    # Take second number
    num2 = int(input("Enter second number: "))

    # Check division by zero
    if num2 != 0:
        # Call division function and print the result
        print("Answer =", division(num1, num2))
    else:
        print("Error! Division by zero is not allowed.")

# Invalid Choice
else:
    print("Invalid Choice! Please select a number between 1 and 4.")