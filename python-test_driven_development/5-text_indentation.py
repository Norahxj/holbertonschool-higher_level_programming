#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Strip leading/trailing spaces
    text = text.strip()
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            print(result.strip())
            print()
            result = ""
    if result:
        print(result.strip())
