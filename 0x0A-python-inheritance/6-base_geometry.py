#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""


class BaseGeometry:
    """
    class Base has public instance
    """
    def area(self):
        """
        function that raises exception
        """
        raise Exception("area() is not implemented")
