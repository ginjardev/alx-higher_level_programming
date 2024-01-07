#!/usr/bin/python3
""" This model defines a class Square with a `size`
and position attributes and instance methods
"""


class Square:
    """A simple python class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method initializes instance object
        Args:
            size (int, optional): size parameter for Square class
            position (tuple, optional): position parameter of square class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """getter method, gets size attribute
        Returns:
            int: size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method, sets size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter method, gets position attribute
        Returns:
            tuple: position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter method, sets position attribute"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates area of a square

        Returns:
            int: the area of square
        """
        return self.__size**2

    def my_print(self):
        """prints square based on size attribute"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
