#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    count = 0
    for i in range(len(my_list)):
        if (new_list.count(my_list[i]) < 1 or len(new_list) == 0):
            new_list.append(my_list[i])
    count = sum([item for item in new_list])
    return count
