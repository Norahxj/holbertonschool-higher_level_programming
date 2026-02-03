#!/usr/bin/python3
"""provides function to convert object to dictionary for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of object for JSON serialization."""
    return obj.__dict__
