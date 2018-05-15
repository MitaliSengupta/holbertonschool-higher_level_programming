#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""


class BaseGeometry:
    """
    class Base has 2 public instances
    """
    def area(self):
        """
        function that raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle with private height and width
    """
    def __init__(self, width, height):
        """
        instantiation of class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        string representation of the rectangle
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
