#!/usr/bin/python3
"""
This file contains functiom
that returns the number of lines
of a text file
"""


def number_of_lines(filename=""):
    """
    function returns number of lines
    """
    i = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            i += 1
    return (i)
