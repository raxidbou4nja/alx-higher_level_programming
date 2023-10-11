#!/usr/bin/python3
"""
class_to_json module.

Contains a function that returns a dictionary.
"""


def class_to_json(obj):
    """
    Returns a dictionary description with a simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: The object for which a dictionary description is generated.

    Returns:
        dict: A dictionary containing the attributes and
        their values from the object.
    """
    return obj.__dict__
