#!/usr/bin/python3
"""add all arguments to a list and save them in a python file"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except:
    data = []

save_to_json_file(data + sys.argv[1:], "add_item.json")
