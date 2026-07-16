# Project Name : Student Report
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : This program collects student information,
#                calculates total marks and average marks,
#                and displays a formatted student report.

# Take student's basic information

# Ask the user to enter student's name
name = input("Enter your name: ")

# Ask the user to enter student's age
age = int(input("Enter your age: "))

# Ask the user to enter student's city
city = input("Enter your city: ")

# Take subject marks

# Enter Physics marks
physics_marks = int(input("Enter your Physics marks: "))

# Enter Chemistry marks
chemistry_marks = int(input("Enter your Chemistry marks: "))

# Enter Mathematics marks
math_marks = int(input("Enter your Math marks: "))

# Perform Calculations

# Calculate total marks
total_marks = physics_marks + chemistry_marks + math_marks

# Calculate average marks
average_marks = total_marks / 3

# Display Student Report

print("\n===================================")
print("         STUDENT REPORT")
print("===================================")

# Display student details
print("Name            :", name)
print("Age             :", age)
print("City            :", city)

print("-----------------------------------")

# Display subject marks
print("Physics Marks   :", physics_marks)
print("Chemistry Marks :", chemistry_marks)
print("Math Marks      :", math_marks)

print("-----------------------------------")

# Display calculated results
print("Total Marks     :", total_marks)
print("Average Marks   :", average_marks)

print("===================================")
print("Report Generated Successfully ✅")
print("===================================")