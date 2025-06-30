#!/usr/bin/env python3
"""
This module demonstrates the use of Abstract Base Classes (ABCs) in Python.

It defines an abstract Animal class and concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    This class defines the interface that all animal subclasses must implement.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            str: The sound that the animal makes
        """
        pass


class Dog(Animal):
    """
    Concrete implementation of Animal for dogs.
    """

    def sound(self):
        """
        Return the sound a dog makes.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete implementation of Animal for cats.
    """

    def sound(self):
        """
        Return the sound a cat makes.

        Returns:
            str: "Meow"
        """
        return "Meow"
