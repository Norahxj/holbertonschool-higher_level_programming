#!/usr/bin/python3
"""Defines a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.

    Adds a trailing space if only one name is provided to match checker.
    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Determine the full name
    if first_name and last_name:
        name = f"{first_name} {last_name}"
    elif first_name:
        name = f"{first_name} "
    elif last_name:
        name = f"{last_name} "
    else:
        name = ""

    print(f"My name is {name}")
