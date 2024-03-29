#!/usr/bin/python3
"""This module contains a BaseGeometry clalss"""


class BaseGeometry:
    """A simple geometry class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
