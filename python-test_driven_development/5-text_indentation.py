#!/usr/bin/python3
"""Function that prints text with 2 new lines after '.', '?', and ':'."""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        start = i
        # Find the next punctuation
        while i < length and text[i] not in ".?:":
            i += 1
        # Extract and print the segment before punctuation
        segment = text[start:i].strip()
        if segment:
            print(segment, end="")
        # If current char is punctuation, print it and 2 newlines
        if i < length and text[i] in ".?:":
            print(text[i], end="\n\n")
        i += 1
