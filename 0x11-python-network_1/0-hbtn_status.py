#!/usr/bin/python3
import urllib.request
"""
Script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as reply:
        body = reply.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode(encoding="utf -8")))
