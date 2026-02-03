#!/usr/bin/env python3
"""
task_02_csv.py
Convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Read a CSV file and convert it to JSON format saved in data.json.

    Args:
        csv_filename (str): The input CSV file name.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        # Read CSV and convert each row into a dictionary
        with open(csv_filename, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        # Serialize the list of dictionaries to JSON and save to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)

        return True

    except FileNotFoundError:
        # CSV file does not exist
        return False
    except Exception as e:
        # Handle other exceptions (optional: print(e) for debugging)
        return False
