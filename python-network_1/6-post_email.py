#!/usr/bin/python3
import requests
import sys

"""Documented"""
if __name__ == "__main__":
"""Documented"""
    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(url, data={"email": email})
    print(r.text)
