#!/usr/bin/env python3
"""
This module demonstrates creating a custom iterator that counts iterations.

CountedIterator wraps any iterable and keeps track of how many items
have been iterated over.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items iterated.

    This class wraps any iterable and provides additional functionality
    to track the number of items that have been fetched.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Get the current count of items iterated.

        Returns:
            int: The number of items that have been iterated over
        """
        return self.count

    def __iter__(self):
        """
        Return the iterator object (self).

        Returns:
            CountedIterator: This iterator instance
        """
        return self

    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.

        Returns:
            The next item from the wrapped iterator

        Raises:
            StopIteration: When there are no more items to iterate
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
