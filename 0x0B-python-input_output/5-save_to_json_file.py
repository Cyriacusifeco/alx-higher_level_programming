#!/usr/bin/python3
"""module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj: Object to be written
        filename(str): Filename
    """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
