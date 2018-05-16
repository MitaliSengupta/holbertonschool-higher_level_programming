#!/usr/bin/python3
"""
This module creates a student class
with public attributes and replaces
attributes of student instances using
Json
"""


class Student:
    """
    student class with public instances
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation of attr
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function returns dict repres
        of instance
        """
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})

    def reload_from_json(self, json):
        """
        function that replaces all attrb of the
        student instance
        """
        self.__dict__.update(json)
