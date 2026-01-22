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
    Raises TypeError if values cannot be converted.
    """
    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
