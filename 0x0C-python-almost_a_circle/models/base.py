#!/usr/bin/python3
"""
A Base class to manage object IDs.
"""

import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            cls: The class.
            list_objs (list): A list of instances that inherit from Base.

        Note:
            The filename is based on the class name.

        Example:
            If called from the Rectangle class, it will
            save to "Rectangle.json".
        """
        filename = cls.__name__ + ".json"
        if list_objs:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        else:
            obj_list = []
        json_data = cls.to_json_string(obj_list)

        with open(filename, "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from a JSON string.

        Args:
            json_string (str): A JSON string representing
            a list of dictionaries.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary.

        Args:
            cls: The class.
            **dictionary: A dictionary with attribute values.

        Returns:
            cls: An instance of the class with attributes
            set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.

        Args:
            cls: The class.

        Returns:
            list: List of instances based on the current class
            and data from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                instance_list = [cls.create(**d) for d in dict_list]
                return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file.

        Args:
            cls: The class.
            list_objs (list): A list of instances that inherit from Base.

        Note:
            The filename is based on the class name.

        Example:
            If called from the Rectangle class, it will
            save to "Rectangle.csv".
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                return

            writer.writerow(fieldnames)

            for obj in list_objs:
                row = [getattr(obj, field) for field in fieldnames]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file.

        Args:
            cls: The class.

        Returns:
            list: List of instances based on the current class
            and data from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline="") as file:
                reader = csv.DictReader(file)
                instance_list = []

                for row in reader:
                    if cls.__name__ == "Square":
                        field_names = ["id", "size", "x", "y"]
                    else:
                        field_names = ["id", "width", "height", "x", "y"]

                    data = {}
                    for key, value in row.items():
                        if key in field_names:
                            data[key] = int(value)

                    instance = cls.create(**data)
                    instance_list.append(instance)

                return instance_list
        except FileNotFoundError:
            return []
