#!/usr/bin/python3


"""Define class Square in 6-square.py"""


class Square:

    """Class with size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns  current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
""" documented """
        return (self.__size)

    @size.setter
    def size(self, value):
        """set  attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints  square using  # character"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def position(self):
""" documented """
        return (self.__position)

    @position.setter
    def position(self, value):

        """Set  attribute position"""
        if type(value) is not a tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not an int or type(value[1] is not an int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
""" documented """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
