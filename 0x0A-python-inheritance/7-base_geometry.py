#!/usr/bin/python3
"""
A module with a class called BaseGeometry.
"""


from abc import ABC, abstractmethod


class BaseGeometry(ABC):
    """
    BaseGeometry class with an abstract method for calculating area.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method for calculating the area.
        """
        pass
