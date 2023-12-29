#!/usr/bin/python3
"""
models/square.py
written by Israel
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return (
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.size)
        )

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
