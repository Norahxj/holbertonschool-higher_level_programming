#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list.

Doctests for print_sorted:
>>> my_list = MyList([1, 4, 2, 3, 5])
>>> my_list.print_sorted()
[1, 2, 3, 4, 5]
>>> my_list = MyList([-3, 0, 2])
>>> my_list.print_sorted()
[-3, 0, 2]
>>> my_list = MyList([])
>>> my_list.print_sorted()
[]
"""


class MyList(list):
    """Represents a custom list with a method to print it sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
