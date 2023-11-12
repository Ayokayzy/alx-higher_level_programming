#!/usr/bin/python3

def best_score(a_dictionary):
    biggest_int = 0
    if a_dictionary == None:
        return None
    for key in a_dictionary.keys():
        if a_dictionary[key] > biggest_int:
            biggest_int = a_dictionary[key]
            my_key = key
    return my_key
