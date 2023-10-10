#!/usr/bin/python3
"""
A module with a class called BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry class with an abstract method for calculating area.
    """

    @classmethod
    def area(cls):
        """
        Abstract method for calculating the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
