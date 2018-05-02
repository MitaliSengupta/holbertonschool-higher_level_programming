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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size: size of the square
        setter validating size is int and >= 0

        Raise:
             TypeError and ValueError
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """size: size of the square
        setter validating size is int and >= 0

        Raise:
             TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns area of the square instance
        """
        return (self.size ** 2)

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())
