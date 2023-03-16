#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)
