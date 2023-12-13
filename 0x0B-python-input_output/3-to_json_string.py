#!/usr/bin/python3
"""This module contains function to_json_string(my_obj):"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string):

    Args:
        my_obj: the dictionary to be converted to JSON
    """
    return json.dumps(my_obj)
