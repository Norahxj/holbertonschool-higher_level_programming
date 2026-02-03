#!/usr/bin/env python3
"""
task_01_pickle.py
Serialize and deserialize a custom Python class using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class with attributes: name, age, is_student.
    Supports serialization and deserialization using pickle.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The output pickle file name.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            # Handle any errors silently
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a pickle file.

        Args:
            filename (str): The input pickle file name.

        Returns:
            CustomObject or None: The loaded object, or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError):
            # File not found, malformed, or incompatible
            return None
