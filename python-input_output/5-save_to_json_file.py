#!/usr/bin/python3
"""provides function to save Python object to file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes Python object to text file using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
