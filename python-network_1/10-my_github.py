#!/usr/bin/python3
#Documented
import requests
import sys

#Documented
if __name__ == "__main__":
#Documented
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(fmhirwa, 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))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
