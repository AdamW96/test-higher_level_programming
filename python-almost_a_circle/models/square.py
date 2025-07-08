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

    # ========================================================================
    # Size property (getter and setter)
    # ========================================================================

    @property
    def size(self):
        """
        Getter for size attribute.

        Since a square has equal width and height, we can return either one.
        We return width by convention.

        Returns:
            int: Size of the square (width or height, they're the same)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute with validation.

        This setter assigns the same value to both width and height,
        maintaining the square property. The validation is handled by
        the Rectangle's width setter, so we get the same error messages.

        Args:
            value (int): Size value to set for both width and height

        Raises:
            TypeError: If value is not an integer (from width setter)
            ValueError: If value is <= 0 (from width setter)
        """
        # Set width first (this will trigger validation)
        self.width = value
        # Set height to the same value
        self.height = value

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

    # ========================================================================
    # Update method with *args and **kwargs (Square-specific)
    # ========================================================================

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes using *args and **kwargs.

        *args takes precedence over **kwargs. If *args exists and is not empty,
        **kwargs will be ignored.

        Args:
            *args: Variable length argument list in order for Square:
                   1st argument: id
                   2nd argument: size
                   3rd argument: x
                   4th argument: y

        Examples:
            square.update(89, 2, 3, 4)  # Uses *args: id=89, size=2, x=3, y=4
            square.update(size=10, x=20)  # Uses **kwargs: updates size and x
            square.update(89, 2, size=10)  # Uses *args only, **kwargs ignored

        Note:
            This method overrides Rectangle's update() method because Square
            has a different argument order (size instead of width/height).
        """
        if args:
            # If args exist and is not empty, use *args and ignore **kwargs
            # Square-specific attribute order: id, size, x, y
            attributes = ["id", "size", "x", "y"]

            # Assign each argument to the corresponding attribute
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            # If no args or args is empty, use **kwargs
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    # ========================================================================
    # Dictionary representation method (Square-specific)
    # ========================================================================

    def to_dictionary(self):
        """
        Returns the dictionary representation of Square.

        This method creates a dictionary containing all the Square's
        attributes. This is useful for:
        - JSON serialization
        - Creating copies of objects
        - Updating other instances with the same attributes
        - Data persistence

        Returns:
            dict: Dictionary containing Square attributes with keys:
                  'id', 'size', 'x', 'y'

        Note:
            This method overrides Rectangle's to_dictionary() method because
            Square uses 'size' instead of separate 'width' and 'height'.

        Example:
            square = Square(10, 2, 1, 5)
            dict_repr = square.to_dictionary()
            # Returns: {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
