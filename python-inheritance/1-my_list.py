#!/usr/bin/python3
"""Module, basically"""

class MyList(list):
    """Subclass of list"""


    def print_sorted(self):
        """Print sorted list in ascending order"""
        print(sorted(self))
