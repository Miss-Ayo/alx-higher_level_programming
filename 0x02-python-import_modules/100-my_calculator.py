#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    j = len(argv[1:])
    x = int(argv[1])
    y = int(argv[3])
    if j != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit (1)
    else:
        print("{:d}".format(add(x, y)))
