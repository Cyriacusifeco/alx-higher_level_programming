#!/usr/bin/python3
"""Module containing Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """constructor

        Args:
            first_name(str): First name
            last_name(str): Last name
            age(int): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict representation of the student.

        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.

        Args:
            attrs(list): Optional argument
        """
        if (type(attrs) == list and all(type(attr) == str
                                        for attr in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance

        Args:
            json(dict): key/value pair to replace attributes
        """
        for k, v in *json:
            setattr(self, k, v)
