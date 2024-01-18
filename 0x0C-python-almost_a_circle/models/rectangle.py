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
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    @get_x.setter
    def get_x(self, value):
        self.__x = value

    @property
    def get_y(self):
        return self.__y

    @get_y.setter
    def get_y(self, value):
        self.__y = value
