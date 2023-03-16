$ #!/usr/bin/python3

class Square:
    """This class defines a square with private instance attributes size and position.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Possible error raised:
        TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square object with optional size and position.

        Arguments:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The position of the new square. Defaults to (0, 0).

        Possible error raised:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the current value of the private instance attribute __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the private instance attribute __size.

        Arguments:
            value (int): The new value for __size.

        Possible error raised:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
       """Return the current value of the private instance attribute __position."""
       return self.__position

   @position.setter
   def position(self,value):
       """Set the value of the private instance attribute __position.

       Arguments:
           value (tuple): The new values for __position.

       Possible error raised:
           TypeError: If value is not a tuple or does not contain two positive integers. 
       """
       if type(value) != tuple or len(value) !=2 or type(value[0]) != int or type(value[1]) != int or \
               value[0] < 0 or value[1] < 0 :
           raise TypeError("position must be a tuple of 2 positive integers")
       else :
           self.__position =value

   def area(self):
       """Return the current square area."""
       return self.__size **2

   def my_print(self):
      """Prints in stdout the square with character #"""
      if self.__size == 0 :
          print()
      else :
          print("\n" *self.position[1], end="")
          for i in range(self.size):
              print(" " *self.position[0], end="")
              print("#" *self.size)
