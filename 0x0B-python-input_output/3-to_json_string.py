#!/usr/bin/python3
"""module"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an obj.

    Args:
        my_obj: Object
    """

    return json.dumps(my_obj)
