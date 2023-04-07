#!/usr/bin/python3
import requests
import sys

"""Documented"""
if __name__ == "__main__":
"""Documented"""
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
