#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return

    new_list = []

    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list


if __name__ == "__main__":
    divisible_by_2(my_list=[])
