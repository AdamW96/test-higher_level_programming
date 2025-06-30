#!/usr/bin/env python3
"""
This module demonstrates extending built-in classes by creating a VerboseList.

VerboseList extends the built-in list class to provide notifications
when items are added or removed.
"""


class VerboseList(list):
    """
    A list subclass that prints notifications for modifications.

    This class extends the built-in list class and overrides methods
    that modify the list to provide user feedback.
    """

    def append(self, item):
        """
        Add an item to the end of the list with notification.

        Args:
            item: The item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable with notification.

        Args:
            iterable: An iterable of items to add to the list
        """
        items_count = len(list(iterable))  # Convert to list to count items
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """
        Remove an item from the list with notification.

        Args:
            item: The item to remove from the list

        Raises:
            ValueError: If the item is not in the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item from the list with notification.

        Args:
            index (int): The index of the item to remove (default: -1, last item)

        Returns:
            The item that was removed

        Raises:
            IndexError: If the list is empty or index is out of range
        """
        item = self[index]  # Get the item before removing it
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
