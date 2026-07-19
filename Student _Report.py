# Project Name : Student Report
# Created By : Rishabh Kumar
# Language : Python
# Description : This program stores student details,
# calculates total marks, average, percentage,
# grade and displays a student report.

# Ask student details
name = input("Enter Student Name : ").strip().title()
age = int(input("Enter Student Age : "))
city = input("Enter Student City : ").strip().title()

# Take subject marks
try:
    physics = float(input("Enter Physics Marks : "))
    chemistry = float(input("Enter Chemistry Marks : "))
    mathematics = float(input("Enter Mathematics Marks : "))
except ValueError:
    print("❌ Please enter valid marks.")
    exit()

# Check marks are between 0 and 100
if (
    physics < 0 or physics > 100 or
    chemistry < 0 or chemistry > 100 or
    mathematics < 0 or mathematics > 100
):
    print("❌ Marks should be between 0 and 100.")
    exit()

# Calculate total marks
total = physics + chemistry + mathematics

# Calculate average
average = total / 3

# Calculate percentage
percentage = (total / 300) * 100

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

# Decide result
if percentage >= 33:
    result = "PASS"
else:
    result = "FAIL"

# Display report
print("\n========== STUDENT REPORT ==========")

print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"City       : {city}")

print("\n========== SUBJECT MARKS ==========")

print(f"Physics    : {physics}")
print(f"Chemistry  : {chemistry}")
print(f"Mathematics: {mathematics}")

print("\n========== RESULT ==========")

print(f"Total Marks : {total}/300")
print(f"Average     : {round(average, 2)}")
print(f"Percentage  : {round(percentage, 2)}%")
print(f"Grade       : {grade}")
print(f"Result      : {result}")

print("\n🎉 Report Generated Successfully!")