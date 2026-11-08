"""
Grocery List Module
Author: Jeffrey Antwi
Purpose: Manages a list of grocery items with JSON persistence
Date: October 15, 2024
"""

import json
from pathlib import Path
from item import Item


class GroceryList:
    """A class to manage a grocery list with data persistence."""
    
    def __init__(self, filename="grocery_data.json"):
        """Initialize grocery list and load existing data if available."""
        self.__items = []
        self.__filename = filename
        self.__load_data()
    
    def __load_data(self):
        """Load data from JSON file if it exists."""
        try:
            filepath = Path(self.__filename)
            if filepath.exists():
                with open(filepath, 'r') as file:
                    data = json.load(file)
                    self.__items = [Item.from_dict(item_data) for item_data in data]
                print("Loaded existing grocery list.")
            else:
                print("No existing grocery list found. Starting fresh.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}. Starting with empty list.")
            self.__items = []
    
    def __save_data(self):
        """Save current list to JSON file."""
        try:
            filepath = Path(self.__filename)
            data = [item.to_dict() for item in self.__items]
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=2)
            print("Grocery list saved successfully.")
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_item(self, name, quantity, price):
        """Add a new item to the grocery list."""
        try:
            if quantity <= 0 or price < 0:
                print("Quantity must be positive and price cannot be negative.")
                return False
            
            item = Item(name, quantity, price)
            self.__items.append(item)
            self.__save_data()
            print(f"Added '{name}' to grocery list.")
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            return False
    
    def remove_item(self, index):
        """Remove an item from the grocery list."""
        try:
            if 0 <= index < len(self.__items):
                removed_item = self.__items.pop(index)
                self.__save_data()
                print(f"Removed '{removed_item.get_name()}' from grocery list.")
                return True
            else:
                print("Invalid item index.")
                return False
        except Exception as e:
            print(f"Error removing item: {e}")
            return False
    
    def mark_item_purchased(self, index):
        """Mark an item as purchased."""
        try:
            if 0 <= index < len(self.__items):
                self.__items[index].mark_purchased()
                self.__save_data()
                print(f"Marked '{self.__items[index].get_name()}' as purchased.")
                return True
            else:
                print("Invalid item index.")
                return False
        except Exception as e:
            print(f"Error marking item as purchased: {e}")
            return False
    
    def view_list(self):
        """Display all items in the grocery list."""
        if not self.__items:
            print("\nYour grocery list is empty.")
            return
        
        print("\n===== YOUR GROCERY LIST =====")
        total_cost = 0
        purchased_cost = 0
        
        for i, item in enumerate(self.__items, start=1):
            print(f"{i}. {item}")
            item_total = item.get_total_price()
            if item.get_purchased():
                purchased_cost += item_total
            else:
                total_cost += item_total
        
        print("================================")
        print(f"Cost of purchased items: ${purchased_cost:.2f}")
        print(f"Estimated cost of remaining items: ${total_cost:.2f}")
        print(f"Total list value: ${purchased_cost + total_cost:.2f}")
    
    def get_total_estimated_cost(self):
        """Calculate total estimated cost of unpurchased items."""
        total = 0
        for item in self.__items:
            if not item.get_purchased():
                total += item.get_total_price()
        return total
    
    def get_item_count(self):
        """Return number of items in the list."""
        return len(self.__items)
    
    def get_purchased_count(self):
        """Return number of purchased items."""
        count = 0
        for item in self.__items:
            if item.get_purchased():
                count += 1
        return count