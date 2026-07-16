# Project Name : Student Grade Calculator
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : This program takes student's marks as input
#                and displays the grade based on marks.

# Take marks as input from the user

marks = int(input("Enter student's marks (0-100): "))

# Validate the marks
# Marks should be between 0 and 100

if marks < 0 or marks > 100:
    print("❌ Invalid Marks! Please enter marks between 0 and 100.")

else:

    # Grade A+
    if marks >= 90:
        print("🎉 Grade : A+")

    # Grade A
    elif marks >= 80:
        print("🎉 Grade : A")

    # Grade B
    elif marks >= 70:
        print("👍 Grade : B")

    # Grade C
    elif marks >= 60:
        print("🙂 Grade : C")

    # Grade D (Pass)
    elif marks >= 33:
        print("✅ Grade : D (Pass)")

    # Fail
    else:
        print("❌ Grade : Fail")