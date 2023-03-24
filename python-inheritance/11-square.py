#!/usr/bin/python3
"""Module, basically"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Inherited from Rectangle, basically"""
    def __init__(self, size):
        """i.e. Constructor"""
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """Returns string descr"""
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
