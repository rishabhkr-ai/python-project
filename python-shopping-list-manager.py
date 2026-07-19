# Project Name : Shopping List Manager
# Created By : Rishabh Kumar
# Language : Python
# Description : This program allows the user to add,
# remove, view and manage a shopping list.

# Create a shopping list with some default items
shopping_list = ["Milk", "Bread", "Eggs"]

# Program will keep running until the user exits
while True:

    # Show menu
    print("\n========== Shopping List Manager ==========")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Shopping List")
    print("4. Exit")

    # Take user's choice
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter a number between 1 and 4.")
        continue

    # Add a new item
    if choice == 1:

        item = input("Enter item name: ").strip().title()

        # Check if item name is empty
        if not item:
            print("❌ Item name cannot be empty.")

        # Check if item already exists
        elif item in shopping_list:
            print("❌ Item already exists in the shopping list.")

        else:
            shopping_list.append(item)
            print(f"✅ '{item}' added successfully.")

    # Remove an item
    elif choice == 2:

        item = input("Enter item name to remove: ").strip().title()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"✅ '{item}' removed successfully.")
        else:
            print("❌ Item not found in the shopping list.")

    # Show all items
    elif choice == 3:

        print("\n========== Shopping List ==========")

        # Check if list is empty
        if len(shopping_list) == 0:
            print("Shopping list is empty.")

        else:
            # Display all items with numbering
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

    # Exit the program
    elif choice == 4:

        print("🙏 Thank You for Using Shopping List Manager.")
        break

    # Invalid choice
    else:
        print("❌ Invalid Choice! Please select a number between 1 and 4.")