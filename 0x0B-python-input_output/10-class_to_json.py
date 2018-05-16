#!/usr/bin/python3
"""
This file defines a function that
returns the dictionary descp with
simple data structure for json
serialization of obj
"""


def class_to_json(obj):
    """
    function that returns dict descp
    """
    return (obj.__dict__)
