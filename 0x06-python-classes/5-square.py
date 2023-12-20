#!/usr/bin/python3
""" This model defines a class Square with a `size`
attribute and instance methods
"""


class Square:
    """A simple python class Square"""

    def __init__(self, size=0):
        """The __init__ method initializes instance object
        Args:
            size (int, optional): size parameter for Square class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """getter method, gets size attribute
        Returns:
            int: size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method, sets size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates area of a square

        Returns:
            int: the area of square
        """
        return self.__size**2

    def my_print(self):
        """ prints square based on size attribute"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
