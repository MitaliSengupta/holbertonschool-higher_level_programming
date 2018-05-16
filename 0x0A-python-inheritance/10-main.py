#!/usr/bin/python3
Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle

print(issubclass(Square, Rectangle))
