#!/usr/bin/python3
"""
Square Class

Definition of the Square class.
"""


class Square:
    """
    2D Square Class

    Contains methods for manipulating square objects.
    """

    def __init__(self, size=0):
        """
        Initializes a square of a given size.

        The size of the square is hidden.

        Args:
            size (int): Length of the sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
