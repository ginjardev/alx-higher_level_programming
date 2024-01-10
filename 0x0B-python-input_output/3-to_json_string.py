#!/usr/bin/python3
"""This module returns JSON object from Python object"""
import json


def to_json_string(my_obj):
    """Returns JSON object
    Args:
        my_obj (object): Python object
    """
    return json.dumps(my_obj)