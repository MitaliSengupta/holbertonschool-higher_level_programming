#!/usr/bin/python3
"""
This file contains functions that
reads n lines of a txt file and prints
it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines
    """
    i = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            i += 1
            print(line, end="")
            if nb_lines == i:
                break
