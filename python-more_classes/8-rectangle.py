#!/usr/bin/python3
"""Compare rectangles"""

class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Delete a Rectangle instance"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """Return the string representation of a Rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Return the string representation of a Rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """Retrieve the width of a Rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a Rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of a Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a Rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a Rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of a Rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
