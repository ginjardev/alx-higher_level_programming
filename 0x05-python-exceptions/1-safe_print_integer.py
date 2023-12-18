#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        if isinstance(value, int):
            return True
    except ValueError:
        pass
    else:
        return False


if __name__ == "__main__":
    safe_print_integer(value)
