#!/usr/bin/python3
"""This module returns Python object from JSON"""
import json


def from_json_string(my_str):
    """Function returns Python object from JSON
    Args:
        my_str (str): JSON string
    """
    return json.loads(my_str)
