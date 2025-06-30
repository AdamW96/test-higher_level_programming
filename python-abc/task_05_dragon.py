#!/usr/bin/env python3
"""
This module demonstrates the use of mixins in Python.

Mixins are classes that provide methods to other classes but are not
meant to stand alone. They allow for code reuse and composition.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capability.

    This mixin can be added to any class to give it swimming behavior.
    """

    def swim(self):
        """Provide swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capability.

    This mixin can be added to any class to give it flying behavior.
    """

    def fly(self):
        """Provide flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A dragon class that inherits capabilities from multiple mixins.

    This class demonstrates how mixins can be combined to create
    classes with multiple behaviors without complex inheritance hierarchies.
    """

    def roar(self):
        """
        Dragon-specific behavior.

        This method is unique to the Dragon class and showcases
        that classes can have their own methods in addition to
        those inherited from mixins.
        """
        print("The dragon roars!")
