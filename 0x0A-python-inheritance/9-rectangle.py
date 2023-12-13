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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
