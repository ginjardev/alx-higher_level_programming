#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """A Rectangle class"""

    def __init__(self, width=0, height=0):
        """The __init__ constructor initializes an instance object
        Args:
            width (int): width parameter
            height (int): height parameter
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns object's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns object's width"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
