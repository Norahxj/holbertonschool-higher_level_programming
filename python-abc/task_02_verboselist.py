#!/usr/bin/env python3
"""
This module defines VerboseList, a custom list class that prints notifications
whenever items are added or removed.
"""


class VerboseList(list):
    """
    A custom list that prints notifications whenever items are added or removed.

    Inherits from the built-in list class.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from iterable and print a notification.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list at index (default last) and print a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
