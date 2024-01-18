#!/usr/bin/python3
"""This is a module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A simple Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle object with width, height, x, y and id"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute with value

        Args:
            value (int): integer parameter
        """
        self.__width = value

    @property
    def height(self):
        """Returns height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attribute with value
        Args:
            value (int): int parameter
        """
        self.__height = value

    @property
    def x(self):
        """Returns x atribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x attribute with value
        Args:
            value (int): int parameter
        """
        self.__x = value

    @property
    def y(self):
        """Returns y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y attribute with value

        Args:
            value (int): int parameter
        """
        self.__y = value
