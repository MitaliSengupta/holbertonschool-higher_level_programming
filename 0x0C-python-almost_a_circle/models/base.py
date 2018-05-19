#!/usr/bin/python3
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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
