#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    av = sys.argv
    if len(sys.argv) != 4:
        print(len(sys.argv))
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif av[2] != '+' or av[2] != '-' or av[2] != '*' or av[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif av[2] == '+':
        print("yes")
        add(int(av[1]), int(av[1]))
    elif av[2] == '-':
        sub(int(av[1]), int(av[1]))
    elif av[2] == '*':
        mul(int(av[1]), int(av[1]))
    elif av[2] == '/':
        div(int(av[1]), int(av[1]))
    sys.exit(0)
