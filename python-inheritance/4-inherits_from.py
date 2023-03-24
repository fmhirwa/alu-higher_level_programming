#!/usr/bin/python3
"""Module, basically"""

def inherits_from(obj, a_class):
    """Will return True if obj instance is inherited directly/indirectly, else False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
