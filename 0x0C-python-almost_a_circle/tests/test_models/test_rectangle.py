#!/usr/bin/python3
"""This is test module for Rectangle class"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""
    def setUp(self):
        self.rectangle = Rectangle(2, 3, 4, 5)
    
    def test_rectangle(self):
        self.assertTrue(self.rectangle)
