$ #!/usr/bin/python3

class Square:
    """This class defines a square with a private instance attribute size.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a new Square object with a given size.

        Arguments:
            size (int): The size of the new square.
        """
        self.__size = size
