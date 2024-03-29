#!/usr/bin/python3
""" This module checks is a class is an
    instance of a particular object"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a
        class that inherited (directly or indirectly) from the
        specified class ; otherwise False."""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
