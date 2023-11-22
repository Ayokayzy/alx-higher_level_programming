#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """
        This  initializes the class

        Arguments:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves size of square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the size of the square

        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #:
            if size is equal to zero, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
