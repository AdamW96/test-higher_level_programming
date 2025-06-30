#!/usr/bin/python3
"""
This module provides a function to convert JSON strings to Python objects.
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): JSON string to convert to Python object

    Returns:
        The Python object represented by the JSON string
    """
    return json.loads(my_str)
