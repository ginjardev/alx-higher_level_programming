#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    else:
        for row in matrix:
            print(" ".join("{:d}".format(col) for col in row))


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
