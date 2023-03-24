#!/usr/bin/python3
"""Module, basically"""

class BaseGeometry:
    """Class, basically"""

    def area(self):
        """Method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The Method validates value and type"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
