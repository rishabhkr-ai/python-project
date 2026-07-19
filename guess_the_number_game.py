# Project Name : Guess The Number Game
# Created By : Rishabh Kumar
# Language : Python
# Description : This program generates a random number.
# The player has to guess the correct number.

# Import random module
import random

# Ask player's name
name = input("Enter your name: ").strip().title()

print(f"\n🎮 Welcome {name}!")
print("I have selected a number between 1 and 10.")
print("Let's see if you can guess it!")

# Program keeps running until user chooses to exit
while True:

    # Generate a random number
    secret_number = random.randint(1, 10)

    # Count number of attempts
    attempts = 0

    while True:

        # Take user's guess
        try:
            guess = int(input("\nEnter your guess (1-10): "))
        except ValueError:
            print("❌ Please enter numbers only.")
            continue

        # Check range
        if guess < 1 or guess > 10:
            print("❌ Please enter a number between 1 and 10.")
            continue

        # Increase attempt count
        attempts += 1

        # Compare the guess
        if guess < secret_number:
            print("📉 Too Low! Try Again.")

        elif guess > secret_number:
            print("📈 Too High! Try Again.")

        else:

            print("\n🎉 Congratulations!")
            print(f"✅ Correct Number : {secret_number}")
            print(f"🎯 Attempts : {attempts}")

            # Give player rating
            if attempts == 1:
                print("🏆 Amazing! First Attempt.")

            elif attempts <= 3:
                print("🌟 Excellent!")

            elif attempts <= 5:
                print("👍 Good Job!")

            else:
                print("💪 Keep Practicing!")

            break

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("\n🙏 Thanks for playing!")
        print("See you again 😊")
        break