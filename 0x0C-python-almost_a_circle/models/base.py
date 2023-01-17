#!/usr/bin/python3
"""
This class will be the base of all other classes in this project.
The goal of it is to manage id attribute in all of my future classes
and to avoid duplicating the same code (by extension, same bugs).

"""
import json


class Base:

    """
    Here, we define our base class attribute.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes the base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list-dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON str representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set
        Args:
            **dictionary(dict): key/value pairs of attributes to be assigned to
            an object"""
        if dictionary != {}:

            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)

            elif cls.__name__ == "Square":
                dummy = cls(1)

            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as obj:
                list_dicts = Base.from_json_string(obj.read())
                return [cls.create(**dic) for dic in list_dicts]
        except FileNotFoundError:
            return []
