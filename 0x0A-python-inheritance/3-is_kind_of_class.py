#!/usr/bin/python3
"""Contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of specified class
    Args:
        obj: instance of class a_class
        a_class: class
    """

    if isinstance(obj, a_class):
        return True
    return False
