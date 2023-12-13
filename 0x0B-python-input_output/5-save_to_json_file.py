#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation:

    Args:
        my_obj: object to be written to a text file
        filename: the file
    """
    with open(filename, 'w') as f:
        data = json.dump(my_obj, f)
