#!/usr/bin/python3
"""Module, basically"""

class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        """Print sorted list in ascending order"""
        print(sorted(self)); > 1-my_list.py 

"""Module"""

def is_same_class(obj, a_class):
    """Will return True if object and class are similar, else False"""
    return type(obj) == a_class
