#!/usr/bin/python3
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """
    Return the number of lines in a text file.

    Args:
        filename (str): The name of the file to count lines in.

    Returns:
        int: The number of lines in the file.
    """
    lines = 0
    with open(filename) as file:
        for line in file:
            lines += 1
    return lines
