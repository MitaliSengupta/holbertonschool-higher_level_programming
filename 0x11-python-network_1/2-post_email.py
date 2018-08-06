#!/usr/bin/python3
import urllib
import sys
"""
script that takes in a url and an email, sends a POST request
to the url with the email as parameter and displays body of the
response
"""


if __name__ == "__main__":
    info = {'email': argv[2])
    info = urllib.parse.urlencode(info)
    info = info.encode('ascii')
    url = argv[1]
    reply = urllib.request.Request(url, info)
    with urllib.request.urlopen(reply) as reply:
        print(reply.read().decode(encoding="utf-8"))
