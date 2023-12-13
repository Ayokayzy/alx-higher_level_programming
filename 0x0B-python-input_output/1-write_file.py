#!/usr/bin/python3
"""A module that prints texts to a file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename: the file where texts are written to
        text: the text to be added to the file
    """
    lenstr = 0
    with open(filename, 'w') as f:
        lenstr = f.write(text)
    return lenstr
