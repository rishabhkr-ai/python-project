def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

print("===calcualator===")
print("1. addition")
print("2. subtraction")
print("3. multiplication ") 
print("4. division")

choice = int(input("Enter your choice: "))

if choice == 1:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(addition(num1, num2))
elif choice == 2:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(subtraction(num1, num2))
elif choice == 3:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(multiplication(num1, num2))
elif choice == 4:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(division(num1, num2))
else:
    print("invalid choice")
    
   

 

