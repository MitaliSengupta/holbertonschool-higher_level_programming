#!/usr/bin/python3
import math


class MagicClass:
    """ class that create circle area"""

    def __init__(self, radius=0):
        """ initializing """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ function defining area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ function defining circuference """
        return ((2 * math.pi) * self.__radius)
