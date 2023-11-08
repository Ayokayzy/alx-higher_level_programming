#!/usr/bin/python3

def uniq_add(my_list=[]):
    count = 0
    count = sum([item for item in set(my_list)])
    return count
