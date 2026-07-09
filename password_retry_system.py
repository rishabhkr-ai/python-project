
password = "python123"
max_attempts = 3
while max_attempts > 0:
    user_password = input("Enter your password: ")
    if user_password == password:
        print("access granted")
        print("welcome Rishabh!")
        break
    else:
        print("Password is incorrect. Try again.")
        max_attempts -= 1
        print("Attempts Left:", max_attempts)
else:
    print("account locked")