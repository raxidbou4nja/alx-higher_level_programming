#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the file to read.

    Raises:
        FileNotFoundError: If the file specified by filename is not found.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
