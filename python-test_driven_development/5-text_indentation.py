#!/usr/bin/python3
"""Function that prints text with 2 new lines after ., ?, :"""

def text_indentation(text):
    """Print a text with 2 new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        if text[i] in ".?:":
            print(text[i], end="\n\n")  # 2 new lines
        else:
            start = i
            while i < length and text[i] not in ".?:":
                i += 1
            line = text[start:i].strip()
            if line:
                print(line)
            i -= 1
        i += 1
