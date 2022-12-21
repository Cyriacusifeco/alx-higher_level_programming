#!/usr/bin/python3
"""
Classes and objects are the two main aspects of object oriented programming.
A class creates a new type where objects are instances of the class. In this
module, we attempt to build our Class "Square" from the ground up step by step.

"""


class Square:

    """
    Now, we add more capabilities such that we print square with "#" through a
    method: my_print while maintaining the type and value validation.

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

    def my_print(self):

        """
        A method that prints area with "#"

        """
        if self.__size == 0:
            print()

        else:

            for i in range(self.__size):

                for i in range(self.__size):
                    print("#", end="")

                print()

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
