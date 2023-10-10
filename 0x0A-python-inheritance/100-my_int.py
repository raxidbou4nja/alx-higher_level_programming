#!/usr/bin/python3
"""
A module with a class called MyInt that inherits from int.
"""


class MyInt(int):
    """
    MyInt class that inherits from int with reversed equality and inequality.
    """

    def __init__(self, my_int):
        """
        Initialize a MyInt object with a value my_int.

        Args:
            my_int (int): The integer value to store.
        """
        self.my_int = my_int

    @property
    def my_int(self):
        """
        Get the value of my_int.

        Returns:
            int: The stored integer value.
        """
        return self.__my_int

    @my_int.setter
    def my_int(self, my_int):
        """
        Set the value of my_int and validate that it's an integer.

        Args:
            my_int (int): The integer value to set.

        Raises:
            TypeError: If my_int is not an integer.
        """
        if type(my_int) is not int:
            raise TypeError("my_int must be an integer")
        else:
            self.__my_int = my_int

    def __eq__(self, other):
        """
        Custom equality method that reverses the behavior of ==.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return self.my_int != other

    def __ne__(self, other):
        """
        Custom inequality method that reverses the behavior of !=.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return self.my_int == other
