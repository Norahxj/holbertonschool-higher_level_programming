#!/usr/bin/env python3
"""
This module defines CountedIterator, an iterator wrapper that
keeps track of how many items have been fetched.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the counted iterator.

        Args:
            iterable (iterable): The object to iterate over.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Raises:
            StopIteration: When the iterator is exhausted.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        """
        Return self as an iterator.
        """
        return self

    def get_count(self):
        """
        Return the number of items that have been iterated so far.

        Returns:
            int: Number of items iterated.
        """
        return self.counter
