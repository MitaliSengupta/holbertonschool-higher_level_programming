#!/usr/bin/python3
import json
import csv
"""
This modules contains a class Base
with all its methods and attributes
definition
"""


class Base:
    """
    This class has a private attribute __nb_objects = 0
    a class constructor definition to check for id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of class which checks for id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This functions returns the json string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes the json
        string representation of list_objs
        to a file
        """
        fn = cls.__name__ + ".json"
        ob = []
        if list_objs is not None:
            for i in list_objs:
                ob.append(cls.to_dictionary(i))
        with open(fn, mode="w") as myFile:
            myFile.write(cls.to_json_string(ob))

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list
        of the json string represenation
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        This function returns an instance
        with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ is "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return (temp)

    @classmethod
    def load_from_file(cls):
        """
        This function returns a list
        of instances
        """
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open(fn, mode="r") as myFile:
                lst = cls.from_json_string(myFile.read())
            for i, j in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except:
            pass
        return (lst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This function serializes in csv
        """
        fn = cls.__name__ + ".csv"
        if fn == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(fn, mode="w", newline="") as myFile:
            if list_objs is None:
                writer = csv.writer(myFile)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(myFile, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This function deserializes from csv
        """
        try:
            fn = cls.__name__ + ".csv"
            with open(fn, newline="") as myFile:
                reader = csv.DictReader(myFile)
                lst = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    lst.append(x)
                return ([cls.create(**objt) for objt in lst])
        except FileNotFoundError:
            return ([])
