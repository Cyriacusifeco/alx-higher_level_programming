#!/usr/bin/python3
"""module than coverts obj to json"""


def class_to_json(obj):
    """Returns dict description of class obj.

    Args:
        obj: instance of a Class

    """
    return obj.__dict__
