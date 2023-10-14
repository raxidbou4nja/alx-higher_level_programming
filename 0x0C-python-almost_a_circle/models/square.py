#!/usr/bin/python3
"""
Square class module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square. Defaults to 0.
            y (int, optional): Y-coordinate of the square. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute, sets width and height to the same value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign positional and/or keyword arguments to attributes.

        Args:
            *args: Positional arguments in the order id, size, x, y.
            **kwargs: Keyword arguments to assign to attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }