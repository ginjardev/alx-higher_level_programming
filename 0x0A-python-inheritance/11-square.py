#!/usr/bin/python3
"""Module for a simple Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        """initializes Square class object

        Args:
            size (int): size parameter
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size**2

    def __str__(self):
        """Returns string output of square object"""
        return f'[square] {self.__size}/{self.__size}'
