#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """Represents a custom list with a method to print it sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
