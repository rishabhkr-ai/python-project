# Project Name : Student Management System
# Created By : Rishabh Kumar
# Language : Python
# Description : This program allows the user to
# add, search, update, delete and display student records.

# Store student data in a dictionary
students = {
    "Rishabh": {
        "age": 19,
        "college": "GH Raisoni SkillTech University",
        "course": "B.Tech CSE"
    }
}

# This function checks if the user entered a valid number
def get_valid_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Please enter a valid number.")

# Program keeps running until the user exits
while True:

    # Display menu
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")

    # Take user's choice
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("❌ Please enter a number between 1 and 6.")
        continue

    # Add a new student
    if choice == 1:

        name = input("Enter student name: ").strip().title()

        # Check if name is empty
        if not name:
            print("❌ Name cannot be empty.")
            continue

        # Check if student already exists
        if name in students:
            print("❌ Student already exists.")
            continue

        age = get_valid_int("Enter age: ")
        college = input("Enter college: ").strip()
        course = input("Enter course: ").strip()

        # Save student details
        students[name] = {
            "age": age,
            "college": college,
            "course": course
        }

        print("✅ Student added successfully.")

    # Search a student
    elif choice == 2:

        name = input("Enter student name: ").strip().title()

        if name in students:

            print("\n========== Student Details ==========")
            print("Name    :", name)
            print("Age     :", students[name]["age"])
            print("College :", students[name]["college"])
            print("Course  :", students[name]["course"])

        else:
            print("❌ Student not found.")

    # Update student details
    elif choice == 3:

        name = input("Enter student name: ").strip().title()

        if name in students:

            print("\nEnter new details")

            age = get_valid_int("Enter new age: ")
            college = input("Enter new college: ").strip()
            course = input("Enter new course: ").strip()

            students[name]["age"] = age
            students[name]["college"] = college
            students[name]["course"] = course

            print("✅ Student updated successfully.")

        else:
            print("❌ Student not found.")

    # Delete a student
    elif choice == 4:

        name = input("Enter student name: ").strip().title()

        if name in students:

            del students[name]

            print("✅ Student deleted successfully.")

        else:
            print("❌ Student not found.")

    # Display all students
    elif choice == 5:

        if len(students) == 0:

            print("No student records found.")

        else:

            print("\n========== All Students ==========")

            count = 1

            for name, details in students.items():

                print(f"\nStudent {count}")
                print("Name    :", name)
                print("Age     :", details["age"])
                print("College :", details["college"])
                print("Course  :", details["course"])

                count += 1

            print(f"\nTotal Students : {len(students)}")

    # Exit the program
    elif choice == 6:

        print("\n🙏 Thank You for Using Student Management System.")
        print("Keep Learning Python 🚀")

        break

    # Invalid menu choice
    else:

        print("❌ Invalid choice. Please select a number between 1 and 6.")