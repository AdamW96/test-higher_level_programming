#!/usr/bin/python3
"""
Rectangle module.
Contains the Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    This class represents a rectangle with width, height, and position (x, y).
    All attributes are private with public getter and setter methods for
    data validation and protection.

    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
        __x (int): X coordinate position
        __y (int): Y coordinate position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            id (int, optional): ID value. Defaults to None.
        """
        # Call the super class constructor with id
        super().__init__(id)

        # Assign each argument to the right attribute using setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ========================================================================
    # Width property (getter and setter)
    # ========================================================================

    @property
    def width(self):
        """
        Getter for width attribute.

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): Width value to set
        """
        self.__width = value

    # ========================================================================
    # Height property (getter and setter)
    # ========================================================================

    @property
    def height(self):
        """
        Getter for height attribute.

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): Height value to set
        """
        self.__height = value

    # ========================================================================
    # X property (getter and setter)
    # ========================================================================

    @property
    def x(self):
        """
        Getter for x coordinate attribute.

        Returns:
            int: X coordinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x coordinate attribute.

        Args:
            value (int): X coordinate value to set
        """
        self.__x = value

    # ========================================================================
    # Y property (getter and setter)
    # ========================================================================

    @property
    def y(self):
        """
        Getter for y coordinate attribute.

        Returns:
            int: Y coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y coordinate attribute.

        Args:
            value (int): Y coordinate value to set
        """
        self.__y = value
