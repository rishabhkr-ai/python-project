# Project Name : Student Information + Calculator
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : This program displays student information
#                and performs basic calculator operations
#                using functions.

# Function to display student information
def student_info(name, age):
    """
    Display student's basic information.
    """

    print("\n========== STUDENT INFORMATION ==========")
    print("Student Name :", name)
    print("Student Age  :", age)

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

# Display student details
student_info("Rishabh", 19)

# Display Calculator Menu
print("\n========== CALCULATOR ==========")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user's choice
choice = int(input("\nEnter your choice: "))

# Addition
if choice == 1:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Answer =", addition(num1, num2))

# Subtraction
elif choice == 2:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Answer =", subtraction(num1, num2))

# Multiplication
elif choice == 3:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Answer =", multiplication(num1, num2))

# Division
elif choice == 4:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Check division by zero
    if num2 != 0:
        print("Answer =", division(num1, num2))
    else:
        print("❌ Division by zero is not allowed.")

# Invalid Choice
else:
    print("❌ Invalid Choice! Please select a number from 1 to 4.")