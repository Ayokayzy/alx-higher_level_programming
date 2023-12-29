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
