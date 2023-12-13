#!/usr/bin/python3
"""A module that appends texts to a file"""


def append_write(filename="", text=""):
    """a function that appends a string to the end of a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename: the file where texts are written to
        text: the text to be added to the file
    """
    lenstr = 0
    with open(filename, 'a') as f:
        lenstr = f.write(text)
    return lenstr
