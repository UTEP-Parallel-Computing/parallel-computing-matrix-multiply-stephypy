#!/usr/bin/env python3
import argparse
import numpy as np
import time
import pymp

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
    for row in range(10):
        for col in range(10):
            print(f'{matrix[row][col]} ', end='')
        print('')

def multiply_matrix(mat_a, mat_b, total_threads):
	"""
	Receives two matrices and num of threads
	"""
    matrix = genMatrix(size=len(mat_a), value=0)

    with pymp.Parallel(total_threads) as p:
        p.print("Calculating from thread {} of {}".format(p.thread_num, p.num_threads))
        for i in p.range(len(mat_a)):
            for j in range(len(mat_b[0])):
                for k in range(len(mat_b)):
                    matrix[i][j] += (mat_a[i][k] * mat_b[k][j])
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
    parser.add_argument('-t', '--thread', default=4, type=int,
                        help='The number of threads to be used')
    parser.add_argument('-f', '--filename',
                        help='The name of the file to save the matrix in (optional)')

    args = parser.parse_args()

    mat = genMatrix(args.size, args.value)
    start_time = time.time()
    result = multiply_matrix(mat, mat, args.thread)
    end_time = time.time()
    print("\n%s seconds\n" % (end_time - start_time))
    printSubarray(result)

main()
