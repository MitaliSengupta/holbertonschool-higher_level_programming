#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """
    Square class with private instance attribute size
    """

    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """
        self.__size = size
