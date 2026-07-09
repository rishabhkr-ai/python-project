import random
name = input("Enter your name:")
print("🎮 Welcome to the Guess The Number Game!")
print("i have a between number 1 to 10. try to get it sir")

secret_number = random.randint(1,10)
attempts = 0 

while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Try again.")
            elif guess > secret_number:
                print("Too High! Try again.")
            else:
                print(f"🎉 Congratulations! {name}!")
                print(f"you guessed the number {secret_number}.")
                print(f"you guessed it in {attempts} attempts")
                if attempts  <= 5:
                      print("👌Excellent player!",attempts)
                elif attempts <= 10:
                      print("👍Good Job!",attempts)
                else:
                      print("✍️Keep practicing!",attempts)
                break                