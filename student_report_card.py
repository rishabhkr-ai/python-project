# Project Name : Student Report Card
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : This program takes student's details and
#                marks of five subjects, calculates total,
#                percentage, grade, and pass/fail status.

# Take Student Details

# Enter student's name
name = input("Enter Student Name: ")

# Enter student's roll number
roll_no = input("Enter Roll Number: ")

# Enter student's class
student_class = input("Enter Class: ")

# Take Marks of Five Subjects

english = float(input("Enter English Marks: "))
math = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))

# Calculate Total and Percentage

# Calculate total marks
total = english + math + science + computer + hindi

# Calculate percentage
percentage = total / 5

# Calculate Grade

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

# Check Pass or Fail

if percentage >= 33:
    result = "PASS"

else:
    result = "FAIL"

# Display Student Report Card

print("\n==========================================")
print("           STUDENT REPORT CARD")
print("==========================================")

print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Class        :", student_class)

print("------------------------------------------")

print("English      :", english)
print("Math         :", math)
print("Science      :", science)
print("Computer     :", computer)
print("Hindi        :", hindi)

print("------------------------------------------")

print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)

print("==========================================")
print("🎉 Report Card Generated Successfully!")
print("==========================================")