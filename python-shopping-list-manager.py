# Initialize the predefined shopping list
shopping_list = ["milk", "bread", "eggs"]

while True:
   
    print("\n====== Shopping List ======")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        new_item = input("Enter the item to add: ").strip().lower()
        if new_item:
            shopping_list.append(new_item)
            print(f"Current list: {shopping_list}")
        else:
            print("Item name cannot be empty.")
            
    elif choice == 2:
        remove_item = input("Enter the item to remove: ").strip().lower()
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"Current list: {shopping_list}")
        else:
            print(f"'{remove_item}' is not in your shopping list.")
            
    elif choice == 3:
        print(f"Your shopping list: {shopping_list}")
        
    elif choice == 4:
        print("Thank you for using the service.")
        break
        
    else:
        print("Invalid choice. Please select an option from 1 to 4.")

