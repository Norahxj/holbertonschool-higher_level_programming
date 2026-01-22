#!/usr/bin/python3
"""Function that prints a text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if not text:
        return

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            # Print stripped result, no trailing space
            print(result.strip())
            print()  # second newline
            result = ""
    if result:
        print(result.strip())
