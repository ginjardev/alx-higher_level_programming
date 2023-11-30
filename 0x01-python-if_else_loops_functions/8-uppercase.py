#!/usr/bin/python3

def uppercase(str):
    j = 0
    if len(str) == 0:
        str = " "
    ln = len(str) - 1
    for i in str:
        if ord(i) > 65 and ord(i) > 90:
            print('{}'.format(chr(ord(i)-32)), end="" if j != ln else "\n")
            j = j + 1
        else:
            print('{}'.format(i), end="" if j != ln else "\n")
            j = j + 1
