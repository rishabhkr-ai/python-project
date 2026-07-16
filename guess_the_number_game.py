# Project Name : Guess The Number Game
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : A fun number guessing game where the player
#                has to guess a random number between 1 and 10.

# Import the random module to generate random numbers
import random


# Ask the player to enter their name
name = input("Enter your name: ")


# Welcome message
print("\n🎮 Welcome to the Guess The Number Game!")
print("I have selected a number between 1 and 10.")
print("Try to guess the correct number.\n")


# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)


# Store the number of attempts
attempts = 0


# Run the game until the correct number is guessed
while True:

    # Ask the user to guess a number
    guess = int(input("Enter your guess: "))

    # Increase the attempt counter
    attempts += 1

    # Check if the guessed number is smaller
    if guess < secret_number:
        print("📉 Too Low! Try Again.\n")

    # Check if the guessed number is greater
    elif guess > secret_number:
        print("📈 Too High! Try Again.\n")

    # If the guessed number is correct
    else:
        print(f"\n🎉 Congratulations, {name}!")
        print(f"✅ You guessed the correct number: {secret_number}")
        print(f"🎯 Total Attempts: {attempts}")

        # Give a rating based on the number of attempts
        if attempts <= 5:
            print("🏆 Excellent Player!")

        elif attempts <= 10:
            print("👍 Good Job!")

        else:
            print("📚 Keep Practicing!")

        # Exit the loop because the game is over
        break