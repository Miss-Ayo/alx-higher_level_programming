#!/usr/bin/python3
from ast import arg


if __name__ == "__main__":
    from sys import argv
    sum = 0
    j = len(argv)
    if j == 1:
        print("0")
    for i in argv[1:]:
        sum += int(i)
    print("{:d}".format(sum))
