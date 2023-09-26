#!/usr/bin/python3
"""
Square Class

Definition of the Square class with size property and area method.
"""


class Square:
    """
    Square Class

    Represents a square with size property and methods for manipulating it.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
