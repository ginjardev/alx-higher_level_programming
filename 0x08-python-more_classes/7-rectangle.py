#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """A Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The __init__ constructor initializes an instance object
        Args:
            width (int, optional): width parameter
            height (int, optional): height parameter
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Outputs string representation of rectangle object

        Returns:
            str: returns string version of rectangle object with #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        row = Rectangle.print_symbol * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Outputs formal string representation of Rectangle object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Message on object deletion"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Returns object's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value for width
        Args:
            value (int): integer value
        """
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
        """sets new value for height
        Args:
            value (int): integer value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
