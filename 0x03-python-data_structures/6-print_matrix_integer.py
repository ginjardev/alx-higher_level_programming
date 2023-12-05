#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    else:
        for row in matrix:
            i = 0
            for col in row:
                print('{:d}'.format(col), end=" " if i != 2 else "")
                i = i + 1
            print()
