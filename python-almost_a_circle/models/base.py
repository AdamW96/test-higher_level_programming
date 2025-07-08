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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        This method is the reverse of to_json_string(). It converts a JSON
        string back to a Python list of dictionaries. This is useful for
        deserializing data that was previously saved or transmitted as JSON.

        Args:
            json_string (str): A string representing a list of dictionaries
                              in JSON format

        Returns:
            list: List of dictionaries represented by json_string
                  Returns empty list [] if json_string is None or empty

        Examples:
            Base.from_json_string('[{"id": 1, "name": "test"}]')
            # Returns: [{"id": 1, "name": "test"}]

            Base.from_json_string("[]")
            # Returns: []

            Base.from_json_string(None)
            # Returns: []

            Base.from_json_string("")
            # Returns: []
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        This method saves a list of instances to a JSON file. The filename
        is automatically generated based on the class name. If the file
        already exists, it will be overwritten.

        Args:
            list_objs (list): List of instances that inherit from Base
                             (e.g., list of Rectangle or Square instances)
                             If None, saves an empty list

        File format:
            The filename will be: <Class name>.json
            Examples: Rectangle.json, Square.json

        """
        # Generate filename based on class name
        filename = cls.__name__ + ".json"

        # Open file for writing (overwrites if exists)
        with open(filename, "w") as file:
            if list_objs is None:
                # If list_objs is None, save empty list
                file.write("[]")
            else:
                # Convert each object to dictionary, then to JSON string
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dictionaries)
                file.write(json_string)
