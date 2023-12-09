#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.fromkeys(a_dictionary.keys())
    values = list(a_dictionary.values())

    i = 0
    for key in new_dict.keys():
        for j in range(len(values)):
            new_dict[key] = values[j + i] * 2
            i = i + 1
            break

    return new_dict


if __name__ == "__main__":
    multiply_by_2(a_dictionary)
