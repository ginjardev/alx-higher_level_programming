#!/usr/bin/python3
""" This model defines a class Square with a `size` attribute """


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

    def area(self):
        """Calculates area of a square

        Returns:
            int: the area of square
        """
        return self.__size ** 2
