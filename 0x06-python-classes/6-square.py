#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0,0)):
        """
        This  initializes the class

        Arguments:
            size: size of the square
            position: x, y position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, position=()):
        """ sets the position of the circle

        Args:
            position: represents the position of the square defined
        Raises:
            TypeError: if the position is not a tuple of 2 positive integers
        """
        if (len(position) != 2
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or position[0] < 0
            or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            for ii in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for jj in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("");
