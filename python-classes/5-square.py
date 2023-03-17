#!/usr/bin/python3

"""Define the Square class"""

class Square:
    """Class with a size attribute"""
    # Constructor that initializes the instance"s size attribute
    def __init__(self, size=0):
        """Initialise Square"""
        # Validate that the size parameter is an integer
        if type(size) is not int:
            raise TypeError("size must be an integer")
        # Validate that the size parameter is not negative
        elif size < 0:
            raise ValueError("size must be >= 0")
        # If the size parameter passes both validation checks, set it as the instance"s size attribute
        self.__size = size

    # Instance method that calculates and returns the area of the square
    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    # Getter method for the size attribute
    @property
    def size(self):
        return (self.__size)

    # Setter method for the size attribute
    @size.setter
    def size(self, value):
        """set the attribute size"""
        # Validate that the value parameter is an integer
        if type(value) is not int:
            raise TypeError("size must be an integer")
        # Validate that the value parameter is not negative
        elif value < 0:
            raise ValueError("size must be >= 0")
        # If the value parameter passes both validation checks, set it as the instance"s size attribute
        self.__size = value

    # Instance method that prints a square of a given size using the "#" character
    def my_print(self):
        """Prints the square using the # character"""
        # If the instance"s size attribute is 0, print a blank line and return
        if self.__size == 0:
            print()
            return
        # Otherwise, print a square with "#" characters using nested loops
        for i in range(self.__size):
            print("#" * self.__size)
