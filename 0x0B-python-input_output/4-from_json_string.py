#!/usr/bin/python3
"""
from_json_string module.

Contains a function that returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure (object)
        represented by the JSON string.
    """
    return json.loads(my_str)
