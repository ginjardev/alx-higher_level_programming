#!/usr/bin/python3
"""This module adds all arguments to a Python list, and then save them to a file"""
import json
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def save_list_to_file(filename="add_item.json"):
    """Function saves Python list to file

    Args:
        filename (object): file object/path
    """
    my_list = []
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        save_to_json_file(my_list, filename)

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    save_list_to_file()
