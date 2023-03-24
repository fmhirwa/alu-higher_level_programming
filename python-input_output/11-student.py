#!/usr/bin/python3
"""Task 11 Module, basically"""


class Student:
    """New class student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """JSON representaion of an instance"""
        if attrs is None:
            return self.__dict__

        attrs_dict = {}
        for att in self.__dict__:
            if att in attrs:
                attrs_dict[att] = self.__dict__[att]

        return attrs_dict

    def reload_from_json(self, json):
        """Replacing all attributes od a student insatnce"""
        for att in json:
            if att in set(self.__dict__.keys()):
                self.__dict__[att] = json[att]
