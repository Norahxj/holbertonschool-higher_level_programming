#!/usr/bin/python3
"""Defines a function that prints a square with #."""


def print_square(size=None):
    """Print a square of size 'size' using the character #.

    Args:
        size (int): The size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if size is None:
        raise TypeError("print_square() missing 1 required positional argument: 'size'")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
