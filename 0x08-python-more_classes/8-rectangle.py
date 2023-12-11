#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """ A class that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the variables of the rectangle class

        Args:
            width - width of the rectangle
            height - height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
