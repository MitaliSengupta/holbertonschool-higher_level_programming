#!/usr/bin/python3
"""
This file contains a function to print
text file to stdout without import
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it stdout
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
