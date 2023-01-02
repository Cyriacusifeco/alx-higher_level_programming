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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """
        initializes the attribute; width and height while
        leaving verification for the setter.

        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):

        """
        A public instance method that returns the area
        of Rectangle.

        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Finds the perimeter of Rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return 2 * (self.width + self.height)

    def __str__(self):

        """
        Returns the string form of Rectangle.

        """

        rect_str = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for row in range(self.__height):
            for col in range(self.__width):
                if isinstance(self.print_symbol, list):
                    rect_str += " ".join(str(x) for x in self.print_symbol)
                else:
                    rect_str += Rectangle.print_symbol
            rect_str += "\n"
        return rect_str

    def __repr__(self):

        """
        Returns the string form of Rectangle in official format.

        """

        return f"Rectangle({self.width}, {self.height})"

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

    def __del__(self):

        """
        method to delete class.

        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
