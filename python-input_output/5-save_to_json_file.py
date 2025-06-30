#!/usr/bin/python3
"""
This module provides a function to save objects to JSON files.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to save to file
        filename (str): The name of the file to save to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
