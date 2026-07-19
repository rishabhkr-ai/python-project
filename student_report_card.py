# Project Name : Student Report Card
# Created By : Rishabh Kumar
# Language : Python
# Description : This program takes student details,
# marks of five subjects, calculates total marks,
# percentage, grade and pass/fail result.

# Take student's basic details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
student_class = input("Enter Class: ")

# Take marks of five subjects
english = float(input("Enter English Marks: "))
math = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))

# Calculate total marks
total = english + math + science + computer + hindi

# Calculate percentage
percentage = total / 5

# Decide grade
if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 33:
    grade = "D"

else:
    grade = "F"

# Check pass or fail
if percentage >= 33:
    result = "PASS"
else:
    result = "FAIL"

# Display report card
print("\n========== STUDENT REPORT CARD ==========")

print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Class        :", student_class)

print("\n========== SUBJECT MARKS ==========")

print("English  :", english)
print("Math     :", math)
print("Science  :", science)
print("Computer :", computer)
print("Hindi    :", hindi)

print("\n========== RESULT ==========")

print("Total Marks :", total)
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)
print("Result      :", result)

print("\n🎉 Report Card Generated Successfully!")