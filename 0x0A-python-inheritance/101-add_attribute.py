#!/usr/bin/python3
"""
A module with a function to add an attribute to an object.
"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object.

    Args:
        obj: The object to which the attribute will be added.
        name (str): The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object does not have a
        dictionary (e.g., built-in types).
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
