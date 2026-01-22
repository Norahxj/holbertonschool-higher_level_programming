#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a number, rounding the results to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    matrix must be a list of lists of integers/floats with all rows
    of the same size.
    div must be an integer or float, and cannot be 0.

    Returns a new matrix with each element rounded to 2 decimal places.

    Raises:
        TypeError: if matrix elements are not all numbers
                   or rows have different sizes
                   or div is not a number
        ZeroDivisionError: if div is 0
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, (int, float)) for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
