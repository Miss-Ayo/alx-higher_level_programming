#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    a = i - 1
    str1 = "argument"
    str2 = "arguments"
    print("{:d} {:s}{:s}".format(a, str1 if i <= 2 else str2, "." if i == 1 else ":"))
    for j, s in enumerate(argv):
        if j > 0:
            print("{:d}: {:s}".format(j, s))
