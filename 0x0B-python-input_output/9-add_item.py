#!/usr/bin/python3
import json
from sys import argv
"""
This file contains a function that adds
all arguments to a python list and saves
to a file
"""


save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    new = load_json(filename)
except (ValueError, FileNotFoundError):
    new = []

new = new + argv[1:]
save_json(new, filename)
