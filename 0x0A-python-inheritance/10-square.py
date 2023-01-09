#!/usr/bin/python3
"""BaseGeometry module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """constructor"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
