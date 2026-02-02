#!/usr/bin/python3
"""Module povides function to convert Python object to JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a Python object as a string."""
    return json.dumps(my_obj)
