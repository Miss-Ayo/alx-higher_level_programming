#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = len(argv)
    if (j == 2):
        print("{:d} argument:".format(j - 1))
    else:
        if (j == 1):
            print("{:d} arguments.".format(j - 1))
        else:
             print("{:d} arguments:".format(j - 1))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
