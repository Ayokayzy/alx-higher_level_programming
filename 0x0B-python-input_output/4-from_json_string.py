#!/usr/bin/python3
"""A module containting function from_json_string(my_str)"""
import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string:

    Args:
        my_str: the json string
    """
    return json.loads(my_str)
