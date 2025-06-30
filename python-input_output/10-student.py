#!/usr/bin/python3
"""
This module defines a Student class with filtered JSON serialization capability.
"""


class Student:
    """
    A class that defines a student with selective attribute serialization.

    This class provides a method to convert the student instance to a dictionary
    with optional attribute filtering.
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
