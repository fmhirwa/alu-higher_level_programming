#!/usr/bin/python3
"""Documented"""
import sys
import urllib.error
import urllib.request

"""Documented"""
if __name__ == "__main__":
"""Documented"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
