#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    new_list = list(a_dictionary.items())
    max_ = new_list[0][1]
    key = " "
    for i in range(len(new_list)):
        if new_list[i][1] > max_:
            max_ = new_list[i][1]
            key = new_list[i][0]

    return key


if __name__ == "__main__":
    best_score(a_dictionary)
