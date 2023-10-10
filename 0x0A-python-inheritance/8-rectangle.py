#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
A module with a class called Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate and set the width and height attributes
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
