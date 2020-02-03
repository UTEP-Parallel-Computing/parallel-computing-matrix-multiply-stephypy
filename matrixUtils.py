# Author: Stephanie Galvan

import argparse
import numpy as np
import time


def genMatrix(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0, size)] for row in range(0, size)]

    return matrix


def genMatrix2(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([np.asarray([value for col in range(0, size)]) for row in range(0, size)])

    return matrix


def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ', end='')
        print('')


def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')


def readFromFile(fileName):
    """
    Reads a matrix from a file
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix


def multiply_matrix(mat_a, mat_b):
    """
    Multiplies two square matrices. The function is written in three nested
    loops in order to lengthen the time of the program
    """
    # Resultant
    matrix = genMatrix(size=len(mat_a))

    # Go through first matrix row
    for i in range(len(mat_a)):
        # Go through columns
        for j in range(len(mat_b[0])):
            for k in range(len(mat_b)):
                matrix[i][j] += (mat_a[i][k] * mat_b[k][j])
    return matrix


def enhanced_multiply_matrix(mat_a, mat_b):
    """
    Faster function to multiply matrices.
    Assumptions: the matrix is a square and each matrix has the same value (i.e mat_a is composed of 2s and mat_b is
    composed of 3s)
    """
    value = 0
    i = 0
    # Only the row of mat_a and the column of mat_b would need to be multiplied and added
    for j in range(len(mat_a)):
        value += (mat_a[i][j] * mat_b[j][i])
    matrix = genMatrix(size=len(mat_a), value=value)
    return matrix


def main():
    """
    Used for running as a script
    """

    parser = argparse.ArgumentParser(description=
                                     'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=1024, type=int,
                        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=1, type=int,
                        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename',
                        help='The name of the file to save the matrix in (optional)')

    args = parser.parse_args()

    mat = genMatrix(args.size, args.value)

    if args.filename is not None:
        print(f'Writing matrix to {args.filename}')
        writeToFile(mat, args.filename)

        print(f'Testing file')
        printSubarray(readFromFile(args.filename))
    else:
        printSubarray(mat)

    print('\n')
    # Multiply the two matrices
    result = multiply_matrix(mat, mat)
    # Provide a small subarray of the result
    printSubarray(result)


# Beginning of the program:
start_time = time.time()
main()
end_time = time.time()
# Estimated time is between 4min - 6min (the first approach took around 0.2 - 0.5 seconds which was too fast to compare
# it with parallel programming later on
print("Total time:")
print("%s seconds" % (end_time - start_time))
