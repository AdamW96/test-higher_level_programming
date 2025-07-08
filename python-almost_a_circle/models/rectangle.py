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

        Raises:
            TypeError: If width, height, x, or y is not an integer
            ValueError: If width or height <= 0, or if x or y < 0
        """
        # Call the super class constructor with id
        super().__init__(id)

        # Assign each argument to the right attribute using setters
        # The setters will handle all validation
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ========================================================================
    # Width property (getter and setter with validation)
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
        Setter for width attribute with validation.

        Args:
            value (int): Width value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # ========================================================================
    # Height property (getter and setter with validation)
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
        Setter for height attribute with validation.

        Args:
            value (int): Height value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # ========================================================================
    # X property (getter and setter with validation)
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
        Setter for x coordinate attribute with validation.

        Args:
            value (int): X coordinate value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # ========================================================================
    # Y property (getter and setter with validation)
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
        Setter for y coordinate attribute with validation.

        Args:
            value (int): Y coordinate value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # ========================================================================
    # Area method
    # ========================================================================

    def area(self):
        """
        Returns the area value of the Rectangle instance.

        The area of a rectangle is calculated as width * height.
        Since width and height are always positive integers (due to validation),
        the result will always be a positive integer.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.width * self.height

    # ========================================================================
    # Display method - SIMPLE VERSION (without x and y handling)
    # ========================================================================

    def display(self):
        """
        Prints the Rectangle instance with the character '#' to stdout.

        This method prints a rectangle made of '#' characters.
        The rectangle will have 'height' rows and 'width' columns.
        This version does NOT handle x and y coordinates.

        Example:
            For Rectangle(4, 3), output will be:
            ####
            ####
            ####
        """
        for i in range(self.height):
            print("#" * self.width)

    # ========================================================================
    # String representation method (__str__)
    # ========================================================================

    def __str__(self):
        """
        Returns the string representation of Rectangle instance.

        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            str: String representation of the Rectangle instance

        Example:
            Rectangle(4, 6, 2, 1, 12) returns "[Rectangle] (12) 2/1 - 4/6"
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
