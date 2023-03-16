#!/usr/bin/python3

"""
test documentation

"""

class Square:
    """This class defines a square with a private instance attribute size.

    Attributes:
        __size (int): The size of the square.

     Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square object with an optional size.

         Args:
            size (int): The size of the new square. Defaults to 0.

         Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Return the current value of the private instance attribute __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the private instance attribute __size.

         Args:
            value (int): The new value for __size.

         Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
