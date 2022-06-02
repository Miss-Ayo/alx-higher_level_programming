#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    print("{:d} {:s}{:s}".format(i - 1, "argument" if i <= 2 else "arguments",
                                 "." if i == 1 else ":"))
    for j, s in enumerate(argv):
        if j > 0:
            print("{:d}: {:s}".format(j, s))
