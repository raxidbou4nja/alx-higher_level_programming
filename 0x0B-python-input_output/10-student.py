#!/usr/bin/python3
"""
Module for class Student
"""


class Student:
    """
    A class students that defines a student by:
    Attributes:
        first_name (str): name of student.
        last_name (str): name of student.
        age (int): age of student.
    Methods:
        __init__ - initializes the Student instance.
        to_json - retrieves dictionary representation of the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Retrieves a dictionary representation of the Student.

        Args:
            attr (list): A list of attribute names that are
            to be retrieved.

        Returns:
            dict: A dictionary representing the attributes
            of the Student instance.
        """
        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
