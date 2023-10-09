#!/usr/bin/python3
"""
=============================
Module with the method lookpu
=============================
"""


def lookup(obj):
    """Function for return the attributes for an object"""

    att_and_methods = dir(obj)
    filtered = [item for item in att_and_methods if not item.startswith('_')]
    return (filtered)
