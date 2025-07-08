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
        Since width and height are always positive integers
        the result will always be a positive integer.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.width * self.height

    # ========================================================================
    # Display method - IMPROVED VERSION (with x and y handling)
    # ========================================================================

    def display(self):
        """
        Prints the Rectangle instance with the character '#' to stdout.

        This method prints a rectangle made of '#' characters, taking care
        of x and y coordinates:
        - y: prints y empty lines before the rectangle
        - x: prints x spaces before each row of '#' characters

        Example:
            For Rectangle(2, 3, 2, 2), output will be:
            (empty line)
            (empty line)
              ##
              ##
              ##
        """
        # Print y empty lines for vertical offset
        for i in range(self.y):
            print()

        # Print the rectangle with x spaces for horizontal offset
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

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

    # ========================================================================
    # Update method with *args and **kwargs
    # ========================================================================

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes using *args and **kwargs.

        *args takes precedence over **kwargs. If *args exists and is not empty,
        **kwargs will be ignored.

        Args:
            *args: Variable length argument list in order:
                   1st argument: id
                   2nd argument: width
                   3rd argument: height
                   4th argument: x
                   5th argument: y
            **kwargs: Arbitrary keyword arguments for any attribute.
                     Key represents the attribute name, value represents the new value.

        Examples:
            rect.update(89, 2, 3, 4, 5)  # Uses *args, updates all attributes
            rect.update(width=10, height=20)  # Uses **kwargs, updates width and height
            rect.update(89, 2, width=10)  # Uses *args only, **kwargs ignored
        """
        if args:
            # If args exist and is not empty, use *args and ignore **kwargs
            attributes = ["id", "width", "height", "x", "y"]

            # Assign each argument to the corresponding attribute
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            # If no args or args is empty, use **kwargs
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
