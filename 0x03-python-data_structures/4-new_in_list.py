#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    elif idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = []
        for i in range(len(my_list)):
            if idx != i:
                new_list.append(my_list[i])
            else:
                new_list.append(element)
    return new_list


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
