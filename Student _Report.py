
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
physics_marks = int(input("Enter your physics marks: "))
chemistry_marks = int(input("Enter your chemistry marks: "))
math_marks = int(input("Enter your math marks: "))
total_marks = physics_marks + chemistry_marks + math_marks
average_marks = total_marks / 3

print("===============================")
print("      STUDENT REPORT       ")
print("===============================")
print("name:", name)
print("age:", age)
print("city:", city)
print("physics :", physics_marks)
print("chemistry :", chemistry_marks)
print("math :", math_marks)
print("total marks:", total_marks)
print("average:", average_marks)
