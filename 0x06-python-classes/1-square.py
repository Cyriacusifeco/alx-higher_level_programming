#!/usr/bin/python3
"""
Classes and objects are the two main aspects of object oriented programming.
A class creates a new type where objects are instances of the class. In this
module, we attempt to build our Class "Square" from the ground up step by step.

"""


class Square:

    """
    Next, we create a private instance attribute: size with no capabilities.

    """
    def __init__(self, size=0):

        """
        initializes the attribute; size
        with no type or value verification.

        """

        self._size = size
