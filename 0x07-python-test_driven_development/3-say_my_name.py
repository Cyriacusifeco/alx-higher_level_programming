#!/usr/bin/python3
"""
This module prints strings of First and last name..

"""


def say_my_name(first_name, last_name=""):
    """
    This method accepts First and Last name as arguments
    and prints them. If either of the arguments are not
    strings, a TypeError is raised.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))

    else:
        print("My name is {}".format(first_name))
