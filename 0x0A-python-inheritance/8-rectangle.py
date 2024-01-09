#!/usr/bin/python3
"""A module with Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A simple Rectangle class"""

    def __init__(self, width, height):
        """Initializes Rectangle object

        Args:
            width (int): width parameter
            height (int): height parameter
        """
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
