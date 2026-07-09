
marks = int(input("Enter a number: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    if marks >= 90:
        print("Grade: A+") 
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 33:
        print("Grade: D")
    else:
        print("Grade: Fail")