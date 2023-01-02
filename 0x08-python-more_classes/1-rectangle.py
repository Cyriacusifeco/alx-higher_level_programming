#!/usr/bin/python3
"""
Classes and objects are the two main aspects of object oriented programming.
A class creates a new type where objects are instances of the class. In this
module, we continue to build our Class "Rectangle" from
the ground up step by step.

"""


class Rectangle:

    """
    Next, we build on the private instance attributes with capabilities
    while maintaining the type and value validations,getters & setters.

    """
    def __init__(self, width=0, height=0):

        """
        initializes the attribute; width and height while
        leaving verification for the setter.

        """

        self.__width = width
        self.__height = height

    @property
    def width(self):

        """
        A method that accesses private attribute - width

        """

        return self.__width

    @width.setter
    def width(self, value):

        """
        Responsible for setting the value of our private attribute: width

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):

        """
        For accessing the value of height.

        """
        return self.__height

    @height.setter
    def height(self, value):

        """
        Responsible for setting the value of height.

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
