#!/usr/bin/python3
"""
Base module.
Contains the Base class which manages id attribute for all future classes.
"""


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
