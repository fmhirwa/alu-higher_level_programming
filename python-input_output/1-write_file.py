#!/usr/bin/python3
"""Task 1 Module, basically"""


def write_file(filename="", text=""):
    """Writes a string to text file & returns number of characters"""
    with open(filename, "w") as f:
        return f.write(text)
