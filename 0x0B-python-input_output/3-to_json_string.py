#!/usr/bin/python3
"""
3-to_json_string module
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to be represented as JSON.

    Returns:
        str: A JSON representation of the input object as a string.
    """
    return json.dumps(my_obj)
