#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_lines(filename="", nb_lines=0):
    """
    Print a given number of lines from a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the file.
        nb_lines (int): The number of lines to read from the file.
    """
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
            return

        lines = 0
        for line in file:
            lines += 1

        file.seek(0)

        if nb_lines >= lines:
            print(file.read(), end="")
            return
        else:
            n = 0
            while n < nb_lines:
                print(file.readline(), end="")
                n += 1
