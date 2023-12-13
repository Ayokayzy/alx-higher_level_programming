#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module contains a Rectangle class"""


class Rectangle(BaseGeometry):
    """A simple Rectangle class"""
    def __init__(self, width, height):
        """initializes the class instance
        Args:
            Width: the width of the Rectangle
            height: the height of the rectangle
        """
        self.__width = width
        self.height = self.integer_validator("height", height)
