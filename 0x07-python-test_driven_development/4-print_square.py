#!/usr/bin/python3
"""
This module is for printing squares
Raises:
TypeError:
ValueError:
"""


def print_square(size):
    """
    function to print a square of given size
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print("{}\n".format("#" * size) * size, end="")
