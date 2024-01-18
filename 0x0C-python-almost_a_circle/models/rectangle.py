#!/usr/bin/python3
"""This is a module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A simple Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle object with width, height, x, y and id"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function returns area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Function prints Rectangle to STDOUT"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string represntation of the object Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
