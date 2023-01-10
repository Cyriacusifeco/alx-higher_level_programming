#!/usr/bin/python3
"""module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename(str): Filename
    """

    with open(filename) as f:
        return json.load(f)
