# Project Name : ATM Machine
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : A simple ATM Machine program that allows
#                the user to check balance, deposit money,
#                withdraw money, and exit the system.

# Store the correct ATM PIN
pin = 1234

# Store the initial account balance
balance = 5000


# Ask the user to enter the ATM PIN
user_pin = int(input("Enter your PIN: "))


# Check whether the entered PIN is correct
if user_pin == pin:

    # Login successful message
    print("\n✅ LOGIN SUCCESSFUL")

    # Display ATM Menu
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Ask the user to choose an option
    choice = int(input("\nEnter your choice: "))

    # Option 1 : Check Balance
    if choice == 1:
        print(f"\n💰 Your Current Balance is: ₹{balance}")

    # Option 2 : Deposit Money
    elif choice == 2:

        # Ask the user to enter deposit amount
        deposit_amount = float(input("Enter amount to deposit: ₹"))

        # Calculate new balance
        new_balance = balance + deposit_amount

        # Display updated balance
        print(f"\n✅ ₹{deposit_amount} deposited successfully.")
        print(f"💰 Updated Balance: ₹{new_balance}")

    # Option 3 : Withdraw Money
    elif choice == 3:

        # Ask the user to enter withdrawal amount
        withdraw_amount = float(input("Enter amount to withdraw: ₹"))

        # Check if sufficient balance is available
        if withdraw_amount <= balance:

            # Calculate remaining balance
            new_balance = balance - withdraw_amount

            print(f"\n✅ ₹{withdraw_amount} withdrawn successfully.")
            print(f"💰 Remaining Balance: ₹{new_balance}")

        else:
            print("\n❌ Insufficient Balance.")

    # Option 4 : Exit
    elif choice == 4:
        print("\n🙏 Thank you for using our ATM.")

    # Invalid Choice
    else:
        print("\n❌ Invalid Choice. Please select a valid option.")

# If the entered PIN is incorrect
else:
    print("\n❌ Incorrect PIN. Access Denied.")