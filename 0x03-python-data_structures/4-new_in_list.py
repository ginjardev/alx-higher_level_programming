#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    elif idx < 0:
        return my_list
    elif idx >= len(myList):
        return my_list
    else:
        new_list = []
        for i in range(len(my_list)):
            if idx != my_list[i]:
                new_list[i] = my_list[i]
            else:
                new_list[i] = element
    return new_list


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
