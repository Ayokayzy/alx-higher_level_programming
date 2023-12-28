#!/usr/bin/python3
"""
models/rectangle.py
written by Israel
"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the width as a private property"""
        return self.__width

    @width.setter
    def width(self, width):
        """validates and sets the width

        Args:
            width: width of the rectangle

        Exceptions:
            TypeError - width must be an integer
            ValueError - width must be > 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """ returns the height as a private property"""
        return self.__height

    @height.setter
    def height(self, height):
        """validates and sets the height

        Args:
            height: height of the rectangle

        Exceptions:
            TypeError - height must be an integer
            ValueError - height must be > 0
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ returns the position on the x axis as a private property"""
        return self.__x

    @x.setter
    def x(self, x):
        """validates and sets the position on the x axis

        Args:
            x: position of the rectangle on the x axis

        Exceptions:
            TypeError - x must be an integer
            ValueError - x must be >= 0
        """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ returns the position of the on the y axis as a private property"""
        return self.__y

    @y.setter
    def y(self, y):
        """validates and sets the wposition on the y axis

        Args:
            y: position of the rectangle on the y axis

        Exceptions:
            TypeError - y must be an integer
            ValueError - y must be >= 0
        """

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        )

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print("")
        rect = ""
        for row in range(self.__height):
            for j in range(self.__x):
                rect += " "
            for col in range(self.__width):
                rect += "#"
            rect += "\n"
        print(rect, end="")
