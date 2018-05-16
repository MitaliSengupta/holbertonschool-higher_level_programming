#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from rectangle
    """
    def __init__(self, size):
        """
        class instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
