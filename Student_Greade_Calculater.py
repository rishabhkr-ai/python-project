# Project Name : Student Grade Calculator
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : This program takes student's marks as input
#                and displays the grade based on marks.

# Ask the user to enter marks
marks = int(input("Enter student's marks (0-100): "))

# Check if marks are valid
if marks < 0 or marks > 100:
    print("❌ Invalid Marks! Please enter marks between 0 and 100.")

# Check the grade
else:

    # Marks 90 or above
    if marks >= 90:
        print("🎉 Grade : A+")

    # Marks 80 to 89
    elif marks >= 80:
        print("🎉 Grade : A")

    # Marks 70 to 79
    elif marks >= 70:
        print("👍 Grade : B")

    # Marks 60 to 69
    elif marks >= 60:
        print("🙂 Grade : C")

    # Marks 33 to 59
    elif marks >= 33:
        print("✅ Grade : D (Pass)")

    # Marks below 33
    else:
        print("❌ Grade : Fail")