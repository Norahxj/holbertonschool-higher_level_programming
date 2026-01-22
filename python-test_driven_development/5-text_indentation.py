#!/usr/bin/python3
"""Function that prints text with 2 new lines after ., ?, :"""

def text_indentation(text):
    """Print a text with 2 new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        # If current char is punctuation
        if text[i] in ".?:":
            print(text[i], end="\n\n")  # 2 new lines
        else:
            start = i
            while i < length and text[i] not in ".?:":
                i += 1
            line = text[start:i].strip()
            if line:
                # Only add a newline if this is not the last character
                if i < length:
                    print(line)
                else:
                    print(line, end="")  # no extra newline at end
            i -= 1
        i += 1
