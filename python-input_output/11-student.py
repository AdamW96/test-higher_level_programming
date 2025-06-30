#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization capability.
"""


class Student:
    """
    A class that defines a student with full serialization/deserialization support.

    This class provides methods to convert to JSON representation and reload
    from JSON data, implementing a basic serialization mechanism.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to include. If None, include all.

        Returns:
            dict: Dictionary containing specified or all instance attributes
        """
        if attrs is None:
            return self.__dict__

        # Filter attributes based on the provided list
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
