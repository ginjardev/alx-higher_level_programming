#!/usr/bin/python3
"""This is a module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a simple Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square object with values"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a reperesntation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square

        args:
          1st argument should be the id attribute
          2nd argument should be the size attribute
          3rd argument should be the x attribute
          4th argument should be the y attribute

        kwargs:
          Key=Value pairs
        """
        if args and len(args) > 0:
            if len(args) >= 1 and args[0] is not None:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id" and v is not None:
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    # Public methos to_dictionary
    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
