#!/usr/bin/python3
"""Module that defines a rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializer method that creates a new instance of Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that retrieves the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets the value of the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that retrieves the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets the value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method that returns the string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width) + "\n") * self.__height

    def __repr__(self):
        """Method that returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
