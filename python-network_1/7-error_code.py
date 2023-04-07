#!/usr/bin/python3
"""Documented"""
import requests
import sys

"""Documented"""
if __name__ == "__main__":
"""Documented"""
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
