#!/usr/bin/env python3
"""
task_03_xml.py
Serialize and deserialize a Python dictionary using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): Output XML file name.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")

    # Create root element
    root = ET.Element('data')

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to string

    # Write XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Input XML file name.

    Returns:
        dict: Dictionary constructed from the XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text  # Values are strings by default
        return result
    except (ET.ParseError, FileNotFoundError):
        return None
