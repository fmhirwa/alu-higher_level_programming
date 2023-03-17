#!/usr/bin/python3


"""Define the class Square but different"""


class Square:
    # Constructor to initialize the class with a size attribute and a position
    def init(self, size=0, position=(0, 0)):
        # Check if the size argument is an integer and greater than or equal to zero
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        # Assign the size argument to the private attribute __size
        self.__size = size
    # Method to calculate and return the area of the square
    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    # Getter method to return the value of the private attribute __size
    @property
    def size(self):
        return (self.__size)

    # Setter method to set the value of the private attribute __size
    @size.setter
    def size(self, value):
        """set the attribute size"""
        # Check if the size argument is an integer and greater than or equal to zero
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        # Set the value of the private attribute __size to the size argument
        self.__size = value

    # Method to print the square using the "#" character
    def my_print(self):
        """Prints the square using the # character"""
        # Check if the size of the square is zero
        if self.__size == 0:
            # If it is, print a newline character and return
            print()
            return
        # Loop through the size of the square and print "#" multiplied by the size on each line
        for i in range(self.__size):
            print("#" * self.__size)

    # Getter method to return the value of the private attribute __position
    @property
    def position(self):
        return (self.__position)

    # Setter method to set the value of the private attribute __position
    @position.setter
    def position(self, value):
        """Set the attribute position"""
        # Check if the value argument is a tuple of length 2
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Check if both elements in the tuple are integers
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Check if both elements in the tuple are greater than or equal to zero
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Set the value of the private attribute __position to the value argument
        self.__position = value

    # Method to print the square with the position set by the __position attribute
    def my_print(self):
        # Check if the size of the square is zero
        if self.__size == 0:
            # If it is, print a newline character and return
            print()
            return

        # Print a newline character multiplied by the second element of the __position attribute
        print("\n" * self.__position[1], end="")

        # Loop through the size of the square
        for i in range(self.__size):
            # Print spaces multiplied by the first element of the __position attribute
            print
