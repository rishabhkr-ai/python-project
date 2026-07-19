# Project Name : Student Information + Calculator
# Created By : Rishabh Kumar
# Language : Python
# Description : This program displays student information
# and performs basic calculator operations using functions.

# Function to display student information
def student_info(name, age):
    # Show student's basic details
    print("\n========== STUDENT INFORMATION ==========")
    print("Student Name :", name)
    print("Student Age  :", age)


# Function to add two numbers
def addition(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtraction(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiplication(num1, num2):
    return num1 * num2


# Function to divide two numbers
def division(num1, num2):
    return num1 / num2


# Display student information
student_info("Rishabh", 19)

# Show calculator menu
print("\n========== CALCULATOR ==========")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user's choice
try:
    choice = int(input("\nEnter your choice: "))
except ValueError:
    print("❌ Please enter a valid number.")
    exit()

# Check user's choice
if choice >= 1 and choice <= 4:

    # Take two numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Please enter valid numbers.")
        exit()

# Addition
if choice == 1:
    print("Answer =", addition(num1, num2))

# Subtraction
elif choice == 2:
    print("Answer =", subtraction(num1, num2))

# Multiplication
elif choice == 3:
    print("Answer =", multiplication(num1, num2))

# Division
elif choice == 4:

    # Check division by zero
    if num2 == 0:
        print("❌ Division by zero is not allowed.")
    else:
        print("Answer =", division(num1, num2))

# Invalid choice
else:
    print("❌ Invalid Choice! Please select a number from 1 to 4.")