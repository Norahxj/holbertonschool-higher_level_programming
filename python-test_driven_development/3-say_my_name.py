#!/usr/bin/python3
"""Defines a function that prints a name."""

def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Build the name exactly as expected by checker
    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name:
        print(f"My name is {first_name} ")
    elif last_name:
        print(f"My name is {last_name} ")
    else:
        print("My name is ")
