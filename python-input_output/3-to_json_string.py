#!/usr/bin/python3
"""
This module provides a function to convert objects to JSON strings.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON string

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
