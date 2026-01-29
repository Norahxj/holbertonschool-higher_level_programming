#!/usr/bin/python3
"""Module that defines a function to check if an object is an instance
of a class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass,
    else False.
    """
    return isinstance(obj, a_class)
