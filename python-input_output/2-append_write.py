#!/usr/bin/python3
"""Task 2 Module, basically"""


def append_write(filename="", text=""):
    """appends the file & returns the number of characters"""
    with open(filename, "a") as f:
        return f.write(text)
