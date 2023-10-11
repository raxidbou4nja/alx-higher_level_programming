#!/usr/bin/python3
"""
save_to_json_file module.

Contains a function that writes an Object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object to be serialized and saved to a file.
        filename (str): The name of the file to which the
        object will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
