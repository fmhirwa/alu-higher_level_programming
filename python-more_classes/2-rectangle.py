#!/usr/bin/python3
"""
Module - Rectangle
"""

class Rectangle:
    """
    Class that defines a rectangle
    """


    def init(self, width=0, height=0):
   
        """
        Initialize rectangle
        Args:
        idth (int): width of rectangle
        height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property


    def width(self):
        """
        Return width of rectangle
        """
        return self.__width

    @width.setter


    def width(self, value):
        """
        Set width of rectangle

        Args:
            value (int): value to set width to

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
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
        Return height of rectangle
        """
        return self.__height

    @height.setter


    def height(self, value):
        """
        Set height of rectangle

        Args:
            value (int): value to set height to

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height


    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
