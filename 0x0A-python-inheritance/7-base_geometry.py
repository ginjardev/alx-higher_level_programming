#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate int value

        Args:
          name (str): Name of the value.
          value (int): Value to validate.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
