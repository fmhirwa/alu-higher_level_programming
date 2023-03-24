#!/usr/bin/python3
"""Module, basically"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Subclass to BaseGeometry"""

    def __init__(self, width, height):
        """i.e. Constructor"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of a rectangle"""
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
