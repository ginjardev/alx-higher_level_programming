#!/usr/bin/python3


def uniq_add(my_list=[]):
    check = 0
    sum = 0
    for i in my_list:
        for j in my_list:
            if i == j:
                check = check + 1
        if check == 1:
            sum = sum + i
        check = 0

    return sum


if __name__ == "__main__":
    uniq_add(my_list=[])
