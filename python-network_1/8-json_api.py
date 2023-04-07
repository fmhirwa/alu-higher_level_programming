#!/usr/bin/python3
"""Documented"""

import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        json_dict = r.json()
        if json_dict:
            print("[{}] {}".format(json_dict.get("id"), json_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
