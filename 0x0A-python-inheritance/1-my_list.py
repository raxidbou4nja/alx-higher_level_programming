#!/usr/bin/python3
"""
A custom class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    A class that extends the list class and adds
    a method for sorting and printing the list.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """

        sorted_list = sorted(self)

        print(sorted_list)
