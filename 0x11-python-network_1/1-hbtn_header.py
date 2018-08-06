#!/usr/bin/python3
import urllib.request
import sys
"""
Script that sends a request to given url
displays the value of X-Request-Id variable
"""


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as reply:
        print(reply.getheader('X-Request-Id'))
