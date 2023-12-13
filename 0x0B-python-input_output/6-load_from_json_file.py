#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”

    Args:
        filename: the file
    """
    data = {}
    with open(filename) as f:
        data = json.load(f)
    return data
