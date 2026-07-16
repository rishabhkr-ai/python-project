# Project Name : Shopping List Manager
# Created By   : Rishabh Kumar
# Language     : Python
# Description  : A simple Shopping List Manager that allows
#                the user to add, remove, view items,
#                and exit the program.

# Create a predefined shopping list
shopping_list = ["milk", "bread", "eggs"]

# Keep the program running until the user chooses Exit
while True:

    # Display the menu
    print("\n========== SHOPPING LIST MANAGER ==========")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")

    # Take user choice
    # Use try-except to prevent program crash
    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("\n❌ Invalid Input!")
        print("Please enter a number between 1 and 4.")
        continue

    # Option 1 : Add Item
    if choice == 1:

        # Take item name from user
        new_item = input("Enter the item to add: ").strip().lower()

        # Check if the item is not empty
        if new_item:

            # Add item to the shopping list
            shopping_list.append(new_item)

            print("\n✅ Item added successfully.")
            print("Current Shopping List:")
            print(shopping_list)

        else:
            print("\n❌ Item name cannot be empty.")

    # Option 2 : Remove Item
    elif choice == 2:

        # Ask user which item they want to remove
        remove_item = input("Enter the item to remove: ").strip().lower()

        # Check if the item exists in the list
        if remove_item in shopping_list:

            # Remove the item
            shopping_list.remove(remove_item)

            print("\n✅ Item removed successfully.")
            print("Current Shopping List:")
            print(shopping_list)

        else:
            print(f"\n❌ '{remove_item}' is not in your shopping list.")

    # Option 3 : Show Shopping List
    elif choice == 3:

        print("\n🛒 Your Shopping List:")

        # Display all items one by one
        for item in shopping_list:
            print("•", item)

    # Option 4 : Exit Program
    elif choice == 4:

        print("\n🙏 Thank you for using Shopping List Manager.")
        break

    # Invalid Choice
    else:

        print("\n❌ Invalid Choice!")
        print("Please select a number between 1 and 4.")