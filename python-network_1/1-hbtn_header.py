#!/usr/bin/python3
#Documented
import sys
import urllib.request

#Documented
if __name__ == "__main__":
#Documented
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
