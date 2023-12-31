#!/usr/bin/python3

"""
models/base.py
written by Israel
"""
import json


class Base:
    """Base class to manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class variables

        Args:
            id - instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        string = json.dumps(list_dictionaries)
        return string

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list = []
        if list_objs is None:
            new_list = []
        else:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())

        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
