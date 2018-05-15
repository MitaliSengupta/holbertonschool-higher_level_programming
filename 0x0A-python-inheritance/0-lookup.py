#!/usr/bin/python3
"""
This module contains a function that returns
the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes, methods and objects
    """
    return (dir(obj))
