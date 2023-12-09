#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None


if __name__ == "__main__":
    best_score(a_dictionary)
