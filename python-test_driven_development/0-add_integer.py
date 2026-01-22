#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Returns the sum of a and b as integers.

    a and b must be integers or floats. Floats are cast to int.
    Raises TypeError if input is invalid.
    """
    import math

    # Validate type
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN or infinity before casting
    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise ValueError("a cannot be NaN or infinite")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise ValueError("b cannot be NaN or infinite")

    return int(a) + int(b)
