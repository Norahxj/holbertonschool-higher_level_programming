#!/usr/bin/python3
"""
This module provides a function that adds two integers.

The function validates input types and safely casts floats
to integers before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Floats are cast to integers.
    Raises TypeError if arguments are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b
