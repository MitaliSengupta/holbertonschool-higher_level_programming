#!/usr/bin/python3
import requests
from sys import argv
"""
script takes githut creds and uses to display id
"""


if __name__ == "__main__":
    uid = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in uid:
        print(uid['id'])
    else:
        print(None)
