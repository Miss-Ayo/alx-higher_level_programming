#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    nbrlines = len(matrix)
    nbrcols = len(matrix[0])
    for i in range(0, nbrlines):
        for j in range(0, nbrcols):
            if j == nbrcols - 1:
                print("{:d}".format(matrix[i][j]), end='')
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
        print()
