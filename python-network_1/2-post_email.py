#!/usr/bin/python3
#Documented
import sys
import urllib.parse
import urllib.request

#Documented

if __name__ == "__main__":
#Documented
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
