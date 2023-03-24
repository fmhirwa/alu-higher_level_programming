#!/usr/bin/python3
"""Module, basically"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass to BaseGeometry"""

    def __init__(self, width, height):
        """i.e Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
