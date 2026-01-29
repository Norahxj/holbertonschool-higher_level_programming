#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize the square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
