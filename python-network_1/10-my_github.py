#!/usr/bin/python3
"""Documented"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
