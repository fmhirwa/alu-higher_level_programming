#!/usr/bin/python3
"""Task 8 Module, basically"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structur"""
    return obj.__dict__
