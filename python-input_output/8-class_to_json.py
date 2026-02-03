#!/usr/bin/python3
"""Module provides function to convert object to dictionary for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization."""
    return obj.__dict__
