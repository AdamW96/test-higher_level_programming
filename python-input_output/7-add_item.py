#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.

This script loads existing items from add_item.json, adds command line arguments,
and saves the updated list back to the file.
"""
import sys

# Import functions from previous exercises
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Filename to store the list
filename = "add_item.json"

# Try to load existing list from file
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with empty list
    items = []

# Add command line arguments to the list (excluding script name)
items.extend(sys.argv[1:])

# Save the updated list to file
save_to_json_file(items, filename)
