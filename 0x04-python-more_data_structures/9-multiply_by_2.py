#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_d = {}
    for key, item in a_dictionary.items():
        new_d[key] = item * 2
        #print("{}: {}".format(key, item))
    return new_d
