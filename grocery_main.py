"""
Grocery Store Checklist Application
Author: Jeffrey Antwi
Purpose: Main application for managing a grocery list with price tracking and data persistence
Date: October 15, 2024
Note: This project demonstrates modular design, OOP, file I/O, exception handling, and data persistence.
"""

from grocery_list import GroceryList


def display_menu():
    """Display the main menu options."""
    print("\n===== GROCERY STORE CHECKLIST =====")
    print("1. Add Item to List")
    print("2. View Grocery List")
    print("3. Mark Item as Purchased")
    print("4. Remove Item from List")
    print("5. Calculate Estimated Total Cost")
    print("6. Exit")
    print("===================================")


def add_item_app(grocery_list):
    """Handle adding an item to the grocery list."""
    print("\n--- Add New Item ---")
    name = input("Enter item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity needed: "))
        if quantity <= 0:
            print("Quantity must be a positive number.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    try:
        price = float(input("Enter price per item ($): "))
        if price < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    grocery_list.add_item(name, quantity, price)


def view_list_app(grocery_list):
    """Handle viewing the grocery list."""
    grocery_list.view_list()


def mark_purchased_app(grocery_list):
    """Handle marking an item as purchased."""
    if grocery_list.get_item_count() == 0:
        print("No items to mark as purchased.")
        return

    grocery_list.view_list()
    try:
        index = int(input("Enter item number to mark as purchased: "))
        if 1 <= index <= grocery_list.get_item_count():
            grocery_list.mark_item_purchased(index - 1)
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_item_app(grocery_list):
    """Handle removing an item from the list."""
    if grocery_list.get_item_count() == 0:
        print("No items to remove.")
        return

    grocery_list.view_list()
    try:
        index = int(input("Enter item number to remove: "))
        if 1 <= index <= grocery_list.get_item_count():
            grocery_list.remove_item(index - 1)
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")


def calculate_total_app(grocery_list):
    """Handle calculating total estimated cost."""
    total = grocery_list.get_total_estimated_cost()
    print(f"\nEstimated Total Cost for Remaining Items: ${total:.2f}")
    print("Note: This excludes items already marked as purchased.")


def main():
    """Main function to run the grocery store checklist application."""
    print("Welcome to the Grocery Store Checklist!")
    print("This application helps you track your shopping list and estimated costs.")
    
    # Initialize grocery list (loads existing data if available)
    grocery_list = GroceryList()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_item_app(grocery_list)
        elif choice == "2":
            view_list_app(grocery_list)
        elif choice == "3":
            mark_purchased_app(grocery_list)
        elif choice == "4":
            remove_item_app(grocery_list)
        elif choice == "5":
            calculate_total_app(grocery_list)
        elif choice == "6":
            print("Goodbye! Have a great day and safe shopping!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()