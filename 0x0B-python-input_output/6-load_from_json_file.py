#!/usr/bin/python3
"""
load_from_json_file module.

Contains a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read
        and deserialize.

    Returns:
        object: The Python object created from the JSON
        data in the file.
    """
    # Open the file in read mode ('r') to read the JSON data
    with open(filename, 'r') as file:
        return json.load(file)
