#!/usr/bin/python3
"""
This module provides a function to load objects from JSON files.
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to load from

    Returns:
        The Python object loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
