"""
Test Suite for Grocery Store Checklist
Author: Jeffrey Antwi
Purpose: Automated testing for Item and GroceryList classes
"""

import pytest
import os
from item import Item
from grocery_list import GroceryList

class TestItem:
    def test_item_creation(self):
        """Test that an item can be created with valid parameters."""
        item = Item("Milk", 2, 3.50)
        assert item.get_name() == "Milk"
        assert item.get_quantity() == 2
        assert item.get_price() == 3.50
        assert item.get_purchased() == False

    def test_item_total_price(self):
        """Test that total price calculation is correct."""
        item = Item("Eggs", 3, 4.00)
        assert item.get_total_price() == 12.00

    def test_item_mark_purchased(self):
        """Test that an item can be marked as purchased."""
        item = Item("Bread", 1, 2.50)
        assert item.get_purchased() == False
        item.mark_purchased()
        assert item.get_purchased() == True

class TestGroceryList:
    def teardown_method(self):
        """Clean up test data file after each test."""
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")

    def test_add_item(self):
        """Test that items can be added to the grocery list."""
        grocery_list = GroceryList("test_data.json")
        assert grocery_list.add_item("Test Item", 1, 1.00) == True
        assert grocery_list.get_item_count() == 1

    def test_add_invalid_item(self):
        """Test that invalid items are rejected."""
        grocery_list = GroceryList("test_data.json")
        assert grocery_list.add_item("Bad Item", -1, 1.00) == False
        assert grocery_list.add_item("Bad Item", 1, -1.00) == False