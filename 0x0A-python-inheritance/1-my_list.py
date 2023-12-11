#!/usr/bin/python3
""" A simple class Mylist that inherits from the
list object"""


class MyList(list):
    """This class inherits from list object"""
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
