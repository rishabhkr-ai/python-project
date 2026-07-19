# Project Name : ATM Machine
# Created By : Rishabh Kumar
# Language : Python
# Description : This program allows the user to log in
# using a PIN, check balance, deposit money,
# withdraw money and exit the ATM.

# Store ATM PIN
PIN = 1234

# Store account balance
balance = 5000

# Ask user to enter PIN
try:
    user_pin = int(input("Enter your ATM PIN: "))
except ValueError:
    print("❌ Please enter numbers only.")
    exit()

# Check PIN
if user_pin == PIN:

    print("\n✅ Login Successful")

    # ATM menu keeps running until user exits
    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Take menu choice
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("❌ Please enter a number between 1 and 4.")
            continue

        # Check balance
        if choice == 1:

            print(f"\n💰 Current Balance : ₹{balance}")

        # Deposit money
        elif choice == 2:

            try:
                amount = float(input("Enter deposit amount: ₹"))
            except ValueError:
                print("❌ Invalid amount.")
                continue

            # Check amount
            if amount <= 0:
                print("❌ Amount must be greater than zero.")

            else:
                balance += amount
                print(f"\n✅ ₹{amount} deposited successfully.")
                print(f"💰 New Balance : ₹{balance}")

        # Withdraw money
        elif choice == 3:

            try:
                amount = float(input("Enter withdraw amount: ₹"))
            except ValueError:
                print("❌ Invalid amount.")
                continue

            # Check amount
            if amount <= 0:
                print("❌ Amount must be greater than zero.")

            elif amount > balance:
                print("❌ Insufficient Balance.")

            else:
                balance -= amount
                print(f"\n✅ ₹{amount} withdrawn successfully.")
                print(f"💰 Remaining Balance : ₹{balance}")

        # Exit ATM
        elif choice == 4:

            print("\n🙏 Thank You For Using Our ATM.")
            print("Have a Nice Day 😊")
            break

        # Invalid choice
        else:

            print("❌ Invalid Choice. Please select between 1 and 4.")

# Wrong PIN
else:

    print("\n❌ Incorrect PIN.")
    print("Access Denied.")