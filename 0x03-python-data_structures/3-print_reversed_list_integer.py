#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_len = len(my_list)
        for i in range(list_len, 0, -1):
            print("{:d}".format(my_list[i - 1]))
