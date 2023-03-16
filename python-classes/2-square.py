$ #!/usr/bin/python3

class Square:
    """This class defines a square with a private instance attribute size.

    Attributes:
        __size (int): The size of the square.

    Possible error raised:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square object with an optional size.

        Arguments:
            size (int): The size of the new square. Defaults to 0.

        Possible error raised:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
