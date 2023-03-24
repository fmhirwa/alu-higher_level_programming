#!/usr/bin/python3
"""Task 0 Module, basically"""


def read_file(filename=""):
    """Reading the file contents & printing to stdout"""
    with open(filename, "r") as f:
        print(f.read(), end="")
