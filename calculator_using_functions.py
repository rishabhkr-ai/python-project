# Project Name : Calculator Using Functions
# Created By : Rishabh Kumar
# Language : Python
# Description : This program performs basic calculator
# operations using Python functions.

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


# Program keeps running until user exits
while True:

    print("\n========== CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Take menu choice
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("❌ Please enter a number between 1 and 5.")
        continue

    # Exit program
    if choice == 5:
        print("\n🙏 Thank You For Using Calculator.")
        break

    # Check valid choice
    if choice < 1 or choice > 5:
        print("❌ Invalid Choice.")
        continue

    # Take numbers from user
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
    except ValueError:
        print("❌ Please enter valid numbers.")
        continue

    # Addition
    if choice == 1:

        print(f"\n✅ Answer = {addition(num1, num2)}")

    # Subtraction
    elif choice == 2:

        print(f"\n✅ Answer = {subtraction(num1, num2)}")

    # Multiplication
    elif choice == 3:

        print(f"\n✅ Answer = {multiplication(num1, num2)}")

    # Division
    elif choice == 4:

        # Check division by zero
        if num2 == 0:
            print("❌ Division by zero is not allowed.")

        else:
            print(f"\n✅ Answer = {division(num1, num2)}")