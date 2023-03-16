#!/usr/bin/python3
"""
Module documentation

This module defines a Rectangle class that has attributes for width and height.
"""

class Rectangle:
    """
    Class documentation

    Defines a rectangle by width, height and can compute area and perimeter.
    """

    number_of_instances = 0


    def __init__(self, width=0, height=0):
        """
        Method documentation

        Initialize a Rectangle instance with a given width and height.

        Args:
            width (int): The width of the rectangle. Default value is 0.
            height (int): The height of the rectangle. Default value is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property


    def width(self):
        """
        Method documentation

        Retrieves the width attribute.

        Returns:
            The width attribute.
        """
        return self.__width

    @width.setter


    def width(self, value):
        """
        Method documentation

        Sets the width attribute to a given value.

        Args:
            value (int): The value to set the width attribute to.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
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
        Method documentation

        Retrieves the height attribute.

        Returns:
            The height attribute.
        """
        return self.__height

    @height.setter


    def height(self, value):
        """
        Method documentation

        Sets the height attribute to a given value.

        Args:
            value (int): The value to set the height attribute to.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """
        Method documentation

        Computes the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height


    def perimeter(self):
        """
        Method documentation

        Computes the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2


    def __str__(self):
        """
        Method documentation

        Prints the rectangle with "#" characters.

        Returns:
            A string that represents the rectangle with "#" characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for i in range(self.__height))


    def __repr__(self):
        """
        Method documentation

        Returns a string that represents the Rectangle object.

        Returns:
            A string that represents the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)


    def __del__(self):
        """
        Method documentation

        Prints the message "Bye rectangle..." when a Rectangle object is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
