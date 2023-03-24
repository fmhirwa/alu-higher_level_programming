#!/usr/bin/python3
"""Task 6 Module, basically"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename) as f:
        file_data = f.read()
        return json.loads(file_data)
