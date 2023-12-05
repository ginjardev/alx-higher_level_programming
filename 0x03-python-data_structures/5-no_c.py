#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return
    else:
        new_str = ""
        for i in my_string:
            if ord(i) == 99 or ord(i) == 67:
                continue
            else:
                new_str += i
    return new_str


if __name__ == "__main__":
    no_c(my_string)
