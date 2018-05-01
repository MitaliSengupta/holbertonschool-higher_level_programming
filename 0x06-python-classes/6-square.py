#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """"
    Square class with private instance attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Args:
               size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

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

    @property
    def position(self):
        """
        position: gives position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        defines position setter values
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not(type(value[0]) is int and type(value[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns area of the square instance
        """
        return (self.size ** 2)

    def my_print(self):
        """
        prints to the stdout square with # or empty line if 0
        """
        if self.size == 0:
            print()
        for a in range(self.position[1]):
            print()
        for a in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
