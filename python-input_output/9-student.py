#!/usr/bin/python3
"""Task 9 Module, basically"""


class Student:
    """New class student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """JSON representaion of an instance"""
        return self.__dict__
