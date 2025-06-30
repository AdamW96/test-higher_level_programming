#!/usr/bin/python3
"""
This module provides a function to convert class instances to dictionaries.
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes

    Returns:
        dict: Dictionary representation of the object's attributes
    """
    return obj.__dict__
