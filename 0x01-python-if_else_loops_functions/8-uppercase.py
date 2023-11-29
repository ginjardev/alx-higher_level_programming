#!/usr/bin/python3

def uppercase(str):
    count = 1
    for i in str:
        if ord(i) > 65 and ord(i) > 90:
            print('{}'.format(chr(ord(i) - 32)), end="" if count < len(str) else "\n")
            count = count + 1
        else:
            print('{}'.format(i), end="" if count < len(str) else "\n")
            count = count + 1

uppercase("Benjamins")
