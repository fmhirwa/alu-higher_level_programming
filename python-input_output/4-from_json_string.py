#!/usr/bin/python3
"""Task 4 Module, basically"""
import json


def from_json_string(my_str):
    """Returns a python data structure represented by JSON"""
    return json.loads(my_str)
