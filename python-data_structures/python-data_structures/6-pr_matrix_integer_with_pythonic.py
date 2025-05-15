#!/usr/bin/python3
# file: print matrix intger with pythonic style
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))

print_matrix_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
