def student_info(name, age):
    print("Name:", name)
    print("Age:", age)


def calculator():
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Addition =", num1 + num2)

    elif choice == 2:
        print("Subtraction =", num1 - num2)

    elif choice == 3:
        print("Multiplication =", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Division =", num1 / num2)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid Choice")


# Main Program
student_info("Rishabh", 17)

calculator()