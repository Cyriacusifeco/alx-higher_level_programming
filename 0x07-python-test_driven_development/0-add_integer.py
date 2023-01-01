#!/usr/bin/python3
"""
This module contains the definition of function to add two integers
with a .txt test file at the root of the directory that runs all the
edge cases.
"""


def add_integer(a, b=98):
    """
    A function that adds two integers.
    """
    try:
        a = int(a)

    except (TypeError, ValueError):
        return "a must be an integer"

    try:
        b = int(b)

    except (TypeError, ValueError):
        return "b must be an integer"

    return(a + b)
