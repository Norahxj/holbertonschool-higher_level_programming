#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Raises TypeError if inputs are not integers or floats,
    or if they cannot be converted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except (OverflowError, ValueError):
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        raise TypeError("b must be an integer")
