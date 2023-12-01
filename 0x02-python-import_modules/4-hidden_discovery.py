#!/usr/bin/python3
import hidden_4


def print_names():
    members = dir(hidden_4)
    for member in members:
        if member[:2] != "__":
            print("{:s}".format(member))


if __name__ == "__main__":
    print_names()
