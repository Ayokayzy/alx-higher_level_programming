#!/usr/bin/python3

""" contains a function add_integer """

def add_integer(a, b=98):
    """a function that adds 2 integers.

    Args:
        a: an integer or float with no defualt value
        b: an integer or float with default value of 98

    Exceptions:
        TypeError: a and b must be an integer

    Return:
         an integer addition of a and b
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
