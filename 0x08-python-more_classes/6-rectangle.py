#!/usr/bin/python3
"""
This is the "Rectangle" module.

This module defines a Rectangle class with width and height attributes,
along with methods to calculate its area, perimeter, and provide string,
representation, and deletion behavior. It also includes a class attribute
`number_of_instances` to keep track of the number of instances created.
"""

class Rectangle:
    """
    A class representing a Rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        """Return a human-readable string representation of the rectangle."""
        result = ""
        for i in range(self.__height):
            result += ("#" * self.__width)
            if i != self.__height - 1:
                result += "\n"
        return result

    def __del__(self):
        """Delete the rectangle and print a message."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
