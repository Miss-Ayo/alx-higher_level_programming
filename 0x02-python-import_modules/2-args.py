#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    j = len(argv)
    if (j == 1):
            print('0 arguments.')
    elif(j == 2):
          print("{:d} argument:".format(j - 1))
          for i in range(i, j):
            print ("{:d} : {:s}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(j - 1))
        for i in range(i, j):
            print ("{:d} : {:s}".format(i, argv[i]))
