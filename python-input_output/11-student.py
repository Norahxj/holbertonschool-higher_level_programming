#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and reload capability."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes contained in this list are included.
        Otherwise, all attributes are included.
        """
        if isinstance(attrs, list):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
