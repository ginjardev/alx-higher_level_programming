#!/usr/bin/python3
"""This module creates an Object from a JSON file"""
import json



def load_from_json_file(filename):
    """Function creates object from JSON file

    Args:
        filename (object): filename/path
    """
    with open(filename, encoding='utf-8') as fp:
        return json.load(fp)
