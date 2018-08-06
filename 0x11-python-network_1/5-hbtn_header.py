#!/usr/bin/python3
import requests
from sys import argv
"""
script that takes in a url to send a request to the url
and display the values of the variable X-Request-Id
"""


if __name__ == "__main__":
    reply = requests.get(argv[1])
    print(reply.headers.get('X-Request-Id'))
