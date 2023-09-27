#!/usr/bin/python3
"""
Square Class

This class defines a 2D square and provides methods for manipulating it.
"""


class Square:
    """
    2D Square Class

    Contains methods for manipulating square objects.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        The size of the square is hidden.

        Args:
            size (int): The length of the sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """

        return self.__size ** 2
