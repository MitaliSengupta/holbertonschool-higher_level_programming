#!/usr/bin/python3
"""
This modules contains a class
that inherits from int
"""


class MyInt(int):
    """
    responds opposite to == and !=
    """
    def __eq__(self, other):
        """
        returns opposite of equal
        """
        return (not super().__eq__(other))

    def __ne__(self, other):
        """
        returns opposite of not equal
        """
        return (not super().__ne__(other))
