#!/usr/bin/env python3
"""
Custom object serialization module using pickle.

This module demonstrates how to serialize and deserialize custom Python objects
using the pickle module, which can handle complex Python objects.
"""
import pickle


class CustomObject:
    """
    A custom class that demonstrates pickle serialization and deserialization.

    This class represents an object with basic attributes and provides methods
    to serialize itself to a file and deserialize from a file.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object

        Returns:
            bool: True if serialization successful, False otherwise
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Error serializing object to {filename}: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject: The deserialized object, or None if error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
            return None
        except pickle.UnpicklingError as e:
            print(f"Error: Invalid pickle format in {filename}: {e}")
            return None
        except Exception as e:
            print(f"Error deserializing object from {filename}: {e}")
            return None
