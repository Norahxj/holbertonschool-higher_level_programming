#!/usr/bin/env python3
"""
task_00_basic_serialization.py
Basic serialization module: serialize a Python dictionary to JSON and deserialize it back.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON file name. Overwrites if file exists.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): Input JSON file name.

    Returns:
        dict: Python dictionary loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
