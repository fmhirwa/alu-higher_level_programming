#!/usr/bin/python3


"""
This module contains a Rectangle class
"""


class Rectangle:
    """
    Rectangle Class: defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance with the given width and height
        """
        self.width = width
        self.height = height

    @property


    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter


    def width(self, value):
        """
        Setter method for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property


    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter


    def height(self, value):
        """
        Setter method for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height


    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)


    def __str__(self):
        """
        Returns a string representation of the rectangle using #
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                rect += "#" * self.width
                if i != self.height - 1:
                    rect += "\n"
            return rect
