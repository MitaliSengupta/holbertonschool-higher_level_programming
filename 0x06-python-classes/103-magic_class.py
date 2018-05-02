#!/usr/bin/python3
import dis
import math

class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        
print(dis.dis(MagicClass))
