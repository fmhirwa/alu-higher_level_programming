#!/usr/bin/python3
#Documented
import requests

#Documented
if __name__ == "__main__":
#Documented
    r = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
