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
        if not instance(size, int):
            raise TypeError('size must be an integer')
        elif not size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
