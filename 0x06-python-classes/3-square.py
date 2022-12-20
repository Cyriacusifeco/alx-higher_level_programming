#!/usr/bin/python3
"""
Classes and objects are the two main aspects of object oriented programming.
A class creates a new type where objects are instances of the class. In this
module, we attempt to build our Class "Square" from the ground up step by step.

"""


class Square:

    """
    Next, we create a private instance attribute: size with capabilities
    while maintaining the type and value validation.

    """
    def __init__(self, size=0):

        """
        initializes the attribute; size
        with type and value verification.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """
        A public instance method that returns the square
        of size.

        """

        return (self.__size * self.__size)
