pin = 1234
balance = 5000

user_pin = int(input("Enter your pin: "))

if user_pin == pin:
    print("LOGIN SUCCESSFUL")

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        deposit_amount = float(input("Enter the amount to deposit: "))
        print(f"You have deposited ${deposit_amount}. Your new balance is: ${balance + deposit_amount}")
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= balance:
            print(f"You have withdrawn ${withdraw_amount}. Your new balance is: ${balance - withdraw_amount}")
        else:
            print("Insufficient balance")
    elif choice == 4:
        print("Thank you for using.")
    else:
        print("Invalid choice")