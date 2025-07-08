#!/usr/bin/python3
"""
Base module.
Contains the Base class which manages id attribute for all future classes.
"""
import json


class Base:
    """
    Base class for managing id attribute in all future classes.

    This class will be the "base" of all other classes in this project.
    The goal is to manage id attribute in all future classes and to avoid
    duplicating the same code (by extension, same bugs).

    Attributes:
        __nb_objects (int): Private class attribute to count instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for Base.

        Args:
            id (int, optional): ID value for the instance. If None,
                               auto-increment __nb_objects and use that value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries

        JSON is one of the standard formats for sharing data representation.
        This method converts a list of dictionaries to a JSON string format
        that can be easily stored, transmitted, or processed.

        Args:
            list_dictionaries (list): List of dictionaries to convert

        Returns:
            str: JSON string representation of the list
                 Returns "[]" if list_dictionaries is None or empty

        Examples:
            Base.to_json_string([{"id": 1, "name": "test"}])
            # Returns: '[{"id": 1, "name": "test"}]'

            Base.to_json_string([])
            # Returns: "[]"

            Base.to_json_string(None)
            # Returns: "[]"
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

