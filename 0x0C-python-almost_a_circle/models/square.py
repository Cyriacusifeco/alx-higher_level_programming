#!/usr/bin/python3
"""Contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square

        Args:
            size(int): Size of the square
            x(int): x coordinate of the square
            y(int): y coordinate of the square
            id(int): Identity of the square

        Raises:
            TypeError: If arguments are not integers
            ValueError: If size < 0
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def to_dictionary(self):
        """Returns dict representation of a Square"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
