#!/usr/bin/python3
"""A module with a Student class"""


class Student:
    """A simple Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student class instance

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student object"""
        return self.__dict__
