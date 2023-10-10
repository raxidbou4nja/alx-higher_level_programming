#!/usr/bin/python3
"""
A module with a class called BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry class with methods for calculating
    area and integer validation.
    """

    def area(self):
        """
        Abstract method for calculating the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if a number is an integer and greater than zero.

        Args:
            name (str): The name of the value being
            validated (for error messages).
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
