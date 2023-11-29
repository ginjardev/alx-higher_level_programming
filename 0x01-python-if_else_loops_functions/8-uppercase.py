#!/usr/bin/python3

def uppercase(str):
    j = 1
    ln = len(str)
    for i in str:
        if ord(i) > 65 and ord(i) > 90:
            print('{}'.format(chr(ord(i)-32)), end="" if j < ln else "\n")
            j = j + 1
        else:
            print('{}'.format(i), end="" if j < ln else "\n")
            j = j + 1
