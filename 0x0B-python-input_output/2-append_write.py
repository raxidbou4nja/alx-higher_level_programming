#!/usr/bin/python3
"""
append_write module
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8)
    and return the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append to the file.

    Returns:
        int: The number of bytes (characters) written to the file.
    """
    with open(filename, mode="a", encoding="UTF-8") as file:
        return file.write(text)
