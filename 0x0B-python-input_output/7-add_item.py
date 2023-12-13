#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file:"""
import sys
save_to_json_file = (__import__("5-save_to_json_file")).save_to_json_file
load_from_json_file = (__import__("6-load_from_json_file")).load_from_json_file

filename = "add_item.json"
my_list_1 = load_from_json_file(filename)
my_list = sys.argv[1:] + my_list_1
save_to_json_file(my_list, filename)
