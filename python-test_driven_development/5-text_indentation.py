#!/usr/bin/python3
"""Function that prints text with 2 new lines after ., ?, :"""

def text_indentation(text):
    """Print a text with 2 new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print_char = text[i]
        if print_char in ".?:":
            # print character and 2 newlines, no spaces before/after
            print(print_char)
            print()
        else:
            # collect sequence of characters until next punctuation
            start = i
            while i < length and text[i] not in ".?:":
                i += 1
            line = text[start:i].strip()
            if line:
                print(line)
            i -= 1  # adjust for the loop increment
        i += 1
