#!/usr/bin/python3
"""Module containing the Rectangle class"""


class Rectangle:
    """Rectangle class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        """Return the string representation of the rectangle to recreate a new instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted"""
        print("Bye rectangle...")
