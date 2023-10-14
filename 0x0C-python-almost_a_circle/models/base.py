#!/usr/bin/python3
"""
A Base class to manage object IDs.
"""


class Base:
    """Base class to handle object IDs."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an object's ID.

        Args:
            id (int): The ID of the object, if provided.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
