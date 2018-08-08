#!/usr/bin/python3
from sys import argv
import requests
"""
script takes 2 args and gets 10 commits
"""


if __name__ == "__main__":
    """
    argv[1] = repository
    argv[2] = owner
    """
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1])).json()
    count = 0
    for commit in req:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, name))
        count += 1
        if count == 10:
            break
