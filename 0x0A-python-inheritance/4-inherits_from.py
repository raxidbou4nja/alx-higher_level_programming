#!/usr/bin/python3
"""
A module with a method for checking if an
object is an instance of a class or its subclass.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclass.

    Args:
        obj: The object to check.
        a_class: The class (or superclass) to compare against.

    Returns:
        True if obj is an instance of a_class or its subclass, False otherwise.
    """

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
