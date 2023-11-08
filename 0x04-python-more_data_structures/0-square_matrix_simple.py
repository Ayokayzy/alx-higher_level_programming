#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    result = [list(map(lambda x: x**2, item)) for item in matrix]
    return result
