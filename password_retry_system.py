# Project Name : Password Retry System
# Created By : Rishabh Kumar
# Language : Python
# Description : This program allows the user
# to enter the correct password.
# The user gets only 3 attempts.

# Store the correct password
correct_password = "python123"

# Maximum login attempts
max_attempts = 3

# Count current attempts
attempt = 1

# Program keeps running until attempts are finished
while attempt <= max_attempts:

    # Ask user to enter password
    user_password = input("\nEnter your password: ").strip()

    # Check if password is empty
    if user_password == "":
        print("❌ Password cannot be empty.")
        continue

    # Check password
    if user_password == correct_password:

        print("\n✅ Login Successful")
        print("🎉 Welcome Rishabh!")
        print("😊 Access Granted")

        break

    else:

        # Show remaining attempts
        remaining = max_attempts - attempt

        print("\n❌ Incorrect Password.")

        if remaining > 0:
            print(f"🔁 Attempts Left : {remaining}")

        attempt += 1

# This block runs only if all attempts are used
else:

    print("\n🔒 Account Locked")
    print("❌ You have used all login attempts.")
    print("⏳ Please try again later.")