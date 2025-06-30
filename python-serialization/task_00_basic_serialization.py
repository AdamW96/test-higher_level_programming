#!/usr/bin/env python3
"""
Basic serialization module for Python dictionaries using JSON format.

This module provides functions to serialize Python dictionaries to JSON files
and deserialize JSON files back to Python dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize
        filename (str): The filename of the output JSON file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error serializing data to {filename}: {e}")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: The deserialized Python dictionary, or None if error occurs
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {filename}: {e}")
        return None
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        return None
