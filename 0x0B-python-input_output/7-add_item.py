#!/usr/bin/python3
"""This module adds arguments to Python list, and save them to a file"""
import json
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def save_list_to_file(filename="add_item.json"):
    """Function saves Python list to file

    Args:
        filename (object): file object/path
    """
    # my_list = []
    # try:
    #     my_list = load_from_json_file(filename)
    # except Exception:
    #     save_to_json_file([], filename)

    # my_list.extend(sys.argv[1:])
    # save_to_json_file(my_list, filename)

    # try:
    #     args = load_from_json_file(filename)
    # except FileNotFoundError:
    #     args = []

    # args.extend(sys.argv[1:])
    # save_to_json_file(args, "add_item.json")

    my_list = []

    # create the Python list from the JSON file, and handle errors as needed
    try:
        py_list = load_from_json_file(filename)
    except Exception:
        # let's create the file, it doesn't exist
        save_to_json_file([], filename)

    # add all the arguments to the lists
    argv = sys.argv[1:]
    for arg in argv:
        py_list.append(arg)

    save_to_json_file(py_list, filename)


if __name__ == "__main__":
    save_list_to_file()
