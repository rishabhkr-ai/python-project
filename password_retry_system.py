# Project Name : Password Retry System
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : A simple password authentication system.
#                The user gets only 3 attempts to enter
#                the correct password.

# Store the correct password
password = "python123"

# Maximum number of login attempts
max_attempts = 3


# Keep asking for the password until attempts become 0
while max_attempts > 0:

    # Ask the user to enter the password
    user_password = input("Enter your password: ")

    # Check if the entered password is correct
    if user_password == password:

        # Login successful
        print("\n✅ Access Granted")
        print("🎉 Welcome Rishabh!")

        # Exit the loop because login is successful
        break

    else:
        # Password is incorrect
        print("\n❌ Incorrect Password.")

        # Reduce the remaining attempts by 1
        max_attempts -= 1

        # Show how many attempts are left
        print("Attempts Left:", max_attempts)

# This else block runs only if the while loop
# finishes without executing the break statement.
else:
    print("\n🔒 Account Locked!")
    print("Please try again later.")