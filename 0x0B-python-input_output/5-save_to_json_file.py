#!/usr/bin/python3
"""This module writes Python object to text file in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """Function writes Python object to JSON file

    Args:
        my_obj (object): Python object
        filename (File object): text file
    """
    with open(filename, mode='w', encoding='utf-8') as fp:
        return fp.write(json.dumps(my_obj))

