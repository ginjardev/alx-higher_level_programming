#!/usr/bin/python3
"""This is test module for Base class"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base = Base()
    
    def tearDown(self):
        del self.base

    def test_base(self):
        self.assertTrue(self.base)

    def test_object_id(self):
        print(self.base.id)
        self.assertEqual(self.base.id, 1)
