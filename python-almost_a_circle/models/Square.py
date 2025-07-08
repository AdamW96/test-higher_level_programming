#!/usr/bin/python3
"""
Square module
This module contains the Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    A square is a special rectangle where width and height are equal.
    This class reuses all the functionality of Rectangle but ensures
    that width and height are always the same (size).

    Attributes:
        All attributes are inherited from Rectangle:
        - id: Identity of the instance
        - width: Width of the square (same as height)
        - height: Height of the square (same as width)
        - x: X coordinate position
        - y: Y coordinate position
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square.

        Args:
            size (int): Size of the square (both width and height)
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            id (int, optional): ID value. Defaults to None.

        Note:
            This constructor calls the Rectangle constructor with
            width=size and height=size, ensuring the square property.
            All validation is inherited from Rectangle.
        """
        # Call the super class (Rectangle) constructor
        # Pass size for both width and height to make it a square
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of Square instance.

        Format: [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: String representation of the Square instance

        Example:
            Square(5, 2, 3, 12) returns "[Square] (12) 2/3 - 5"
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
