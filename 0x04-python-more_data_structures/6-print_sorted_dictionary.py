#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    for key in sorted(keys):
        print("{}: {}".format(key, a_dictionary[key]))
