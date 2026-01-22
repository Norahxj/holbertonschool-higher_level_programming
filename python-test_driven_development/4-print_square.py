#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""


def print_square(size):
    """Prints a square of the given size using the '#' character.

    Args:
        size (int): size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
