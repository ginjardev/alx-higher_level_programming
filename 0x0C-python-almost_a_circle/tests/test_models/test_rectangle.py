#!/usr/bin/python3
"""This is test module for Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def setUp(self):
        self.rectangle = Rectangle(2, 3, 4, 5)

    def test_rectangle(self):
        self.assertTrue(self.rectangle)

    def test_width(self):
        self.assertEqual(self.rectangle.width, 2)

    def test_set_width(self):
        self.rectangle.width = 3
        self.assertEqual(self.rectangle.width, 3)

    def test_height(self):
        self.assertEqual(self.rectangle.width, 2)

    def test_set_height(self):
        self.rectangle.height = 4
        self.assertEqual(self.rectangle.height, 4)

    def test_x(self):
        self.assertEqual(self.rectangle.x, 4)

    def test_set_x(self):
        self.rectangle.x = 5
        self.assertEqual(self.rectangle.x, 5)

    def test_y(self):
        self.assertEqual(self.rectangle.y, 5)

    def test_set_y(self):
        self.rectangle.y = 7
        self.assertEqual(self.rectangle.y, 7)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 6)

    def test_str(self):
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (10) 4/5 - 2/3")
