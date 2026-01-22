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
    Raises TypeError if arguments are not integers or floats,
    or if floats cannot be converted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and Infinity explicitly
    if isinstance(a, float) and (a != a or a == float("inf") or a == float("-inf")):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float("inf") or b == float("-inf")):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
