#!/usr/bin/python3
"""Task 5 Module, basically"""
import json


def save_to_json_file(my_obj, filename):
    """Writes obj to txt file using json"""
    with open(filename, "w") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
