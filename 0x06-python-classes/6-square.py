#!/usr/bin/python3
"""
definition of square
"""

class Square:
    """A 2D square class with methods for manipulation."""

    @property
    def size(self):
        """Get or set the length of the square's sides.

        The setter validates that the size is an integer and is non-negative.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be greater than or equal to 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square on a plane.

        The setter validates that the position is a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("Position must be a tuple of two positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """Create a square with a given size and position.

        Args:
            size (int): The length of the sides.
            position (tuple): The position of the square on a plane.

        Raises:
            TypeError: If size is not an integer or position is not a valid tuple.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be greater than or equal to 0")
        self.__size = size

        if not (isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("Position must be a tuple of two positive integers")
        else:
            self.__position = position

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print a grid of '#' characters representing the square.

        Prints a blank line if the size is 0.
        Also, moves the square to match its position on the plane.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
