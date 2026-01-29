#!/usr/bin/python3
"""Module defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Represents the base geometry class."""

    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
