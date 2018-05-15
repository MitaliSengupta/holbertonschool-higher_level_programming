#!/usr/bin/python3
"""
This module has a class MyList that inherits from
list. Has a public instance method print_sorted that
prints the list in ascending order
"""


class MyList(list):
    """
    class that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
