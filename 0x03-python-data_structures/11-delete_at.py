#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list is None:
        return
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                del my_list[i]

    return my_list


if __name__ == "__main__":
    delete_at(my_list=[], idx=0)
