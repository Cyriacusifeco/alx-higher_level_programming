#!/usr/bin/python3
"""
Classes and objects are the two main aspects of object oriented programming.
A class creates a new type where objects are instances of the class. In this
module, we attempt to build our Class "Square" from the ground up step by step.

"""


class Square:

    """
    Next, we build on the private instance attribute:size with capabilities
    while maintaining the type and value validation. Adding getters & setters.

    """
    def __init__(self, size=0):

        """
        initializes the attribute; size while
        leaving verification for the setter.

        """

        self.__size = size

    def area(self):

        """
        A public instance method that returns the square
        of size.

        """

        return (self.__size * self.__size)

    @property
    def size(self):

        """
        A method that accesses private attribute - size

        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        Responsible for setting the value of our private attribute: size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
