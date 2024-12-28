import os

def display_menu():
    print("Shopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

def view_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

def load_list(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_list(shopping_list, filename):
    with open(filename, 'w') as file:
        for item in shopping_list:
            file.write(f"{item}\n")

def main():
    filename = 'shopping_list.txt'
    shopping_list = load_list(filename)
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            save_list(shopping_list, filename)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
