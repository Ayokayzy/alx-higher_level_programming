#!/usr/bin/python3
"""A module that print the text in a file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) 
    and prints it to stdout:

    Args:
        filename: the text file to be read
    """
    with open(filename) as f:
        text = f.read()
        print("{}".format(text), end="")
