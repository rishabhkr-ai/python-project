
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
city = input("Enter student's city: ")
phone_number = input("Enter student's phone number: ")
email = input("Enter student's email: ")
marks1 = int(input("Enter your physics marks : "))
marks2 = int(input("Enter your chemistry marks : "))
marks3 = int(input("Enter your math marks : "))
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

print("Student's name:", name)
print("Student's age:", age)
print("Student's city:", city)
print("Student's phone number:", phone_number)
print("Student's email:", email)
print("Student's physics marks:", marks1)
print("Student's chemistry marks:", marks2)
print("Student's math marks:", marks3)
print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Percentage:", percentage := (total_marks / 300) * 100)
print("Result:", marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and percentage >= 40 and "Pass" or "Fail")