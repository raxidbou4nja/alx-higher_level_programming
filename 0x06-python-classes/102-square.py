#!/usr/bin/python3
class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()
