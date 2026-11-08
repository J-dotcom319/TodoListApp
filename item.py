"""
Item Module
Author: Jeffrey Antwi
Purpose: Represents a single grocery item with name, quantity, price, and purchase status
Date: October 15, 2024
"""

import json


class Item:
    """A class to represent a single grocery item."""
    
    def __init__(self, name, quantity, price, purchased=False):
        """Initialize item with name, quantity, price, and purchase status."""
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__purchased = purchased
    
    def get_name(self):
        """Return item name."""
        return self.__name
    
    def get_quantity(self):
        """Return item quantity."""
        return self.__quantity
    
    def get_price(self):
        """Return item price."""
        return self.__price
    
    def get_purchased(self):
        """Return purchase status."""
        return self.__purchased
    
    def mark_purchased(self):
        """Mark item as purchased."""
        self.__purchased = True
    
    def get_total_price(self):
        """Calculate total price for this item (quantity * price)."""
        return self.__quantity * self.__price
    
    def to_dict(self):
        """Convert item to dictionary for JSON serialization."""
        return {
            "name": self.__name,
            "quantity": self.__quantity,
            "price": self.__price,
            "purchased": self.__purchased
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Item from dictionary (JSON deserialization)."""
        return cls(
            name=data["name"],
            quantity=data["quantity"],
            price=data["price"],
            purchased=data.get("purchased", False)
        )
    
    def __str__(self):
        """String representation of item."""
        status = "✓ PURCHASED" if self.__purchased else "○ NEEDS TO BUY"
        return f"[{status}] {self.__name} (Qty: {self.__quantity}, ${self.__price:.2f} each, Total: ${self.get_total_price():.2f})"