#!/usr/bin/python3
"""
This file contains function that
writes a string to text file and returns
number of characters written
"""


def write_file(filename="", text=""):
    """
    function to write to files
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
