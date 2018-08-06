#!/usr/bin/python3
import requests
from sys import argv
"""
script to send post request to passed url with email and display
body as response
"""


if __name__ == "__main__":
    reply = requests.post(argv[1], {'email': argv[2]})
    print(reply.text)
