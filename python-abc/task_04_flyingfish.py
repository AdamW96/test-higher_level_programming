#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance in Python.

It shows how a class can inherit from multiple parent classes
and how method resolution order (MRO) works.
"""


class Fish:
    """
    A class representing fish with swimming and habitat behaviors.
    """

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """
    A class representing birds with flying and habitat behaviors.
    """

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing flying fish that inherits from both Fish and Bird.

    This class demonstrates multiple inheritance and method overriding.
    The method resolution order (MRO) can be checked using FlyingFish.mro().
    """

    def fly(self):
        """Override the fly method with flying fish specific behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swim method with flying fish specific behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method with flying fish specific behavior."""
        print("The flying fish lives both in water and the sky!")
