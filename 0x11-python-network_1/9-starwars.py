#!/usr/bin/python3
import requests
from sys import argv
"""
script that  takes in a string and sends a search request to the star wars API
"""


if __name__ == "__main__":
    vals = {"search": argv[1] if len(argv) > 1 else ""}
    try:
        req = requests.get('https://swapi.co/api/people/', params=vals).json()
        count = req.get("count")
        print("Number of results: {}".format(count))
        if count > 0:
            for results in req.get("results"):
                print(results["name"])
    except ValueError:
        print("Not a valid JSON")
