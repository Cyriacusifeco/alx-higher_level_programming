#!/usr/bin/python3
"""module"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str(str): JSON string
    """

    return json.loads(my_str)
