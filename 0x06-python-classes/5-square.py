#!/usr/bin/python3
"""
Square Class

Definition of the Square class with properties and methods for manipulating it.
"""


class Square:
    """
    2D Square Class

    Represents a square with size property and methods for calculating area
    and printing a square grid.
    """

    @property
    def size(self):
        """
        int: Length of square sides.

        The setter validates that the size is an integer and is 0 or greater.
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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints out a grid of '#' representing the square.

        Prints a blank line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
