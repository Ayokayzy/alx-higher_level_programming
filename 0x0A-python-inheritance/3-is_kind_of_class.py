#!/usr/bin/python3
""" This module checks is a class is an
    instance of a particular object"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False."""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
