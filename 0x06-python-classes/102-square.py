#!/usr/bin/python3
"""Coordinates of a square"""



class Square:
    """Defines a square with size and comparison methods."""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter method for the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size."""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Equal comparison."""
        return self.size == other.size

    def __ne__(self, other):
        """Not equal comparison."""
        return self.size != other.size

    def __lt__(self, other):
        """Less than comparison."""
        return self.size < other.size

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.size <= other.size

    def __gt__(self, other):
        """Greater than comparison."""
        return self.size > other.size

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.size >= other.size
