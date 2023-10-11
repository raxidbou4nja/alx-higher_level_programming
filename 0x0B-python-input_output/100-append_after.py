#!/usr/bin/python3
"""append_after module.

Contains a function that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each
        line of the file.
        new_string (str): The line of text to insert after each
        line that contains the search string.
    """
    out = ""

    with open(filename, 'r') as f:
        for line in f:
            out += line
            if search_string in line:
                out += new_string

    with open(filename, 'w') as f:
        f.write(out)
