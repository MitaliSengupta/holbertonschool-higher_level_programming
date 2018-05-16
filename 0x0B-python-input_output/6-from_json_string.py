#!/usr/bin/python3
import json
"""
This file contains a function that
returns an object represented by a
JSON string
"""


def from_json_string(my_str):
    """
    function to return object
    represented by a JSON string
    """
    return (json.loads(my_str))
