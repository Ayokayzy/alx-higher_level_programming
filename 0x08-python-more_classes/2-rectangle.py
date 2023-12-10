#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """ A class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes the variables of the rectangle class

        Args:
            width - width of the rectangle
            height - height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the with of the rectangle as a
        private variable"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the with of the rectangle to a private variable
        Args:
            width - the width of the variable

        Exceptions:
            TypeError - width must be an integer
            ValueError - width must be >= 0
        """

        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """ returns the height of the rectangle as a
        private variable"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the with of the rectangle to a private variable
        Args:
            height - the height of the variable

        Exceptions:
            TypeError - height must be an integer
            ValueError - height must be >= 0
        """

        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        """returns the area of the rctangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
