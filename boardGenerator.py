"""
File containing all methods for board generation.
Methods take the form of generators for easy looping.
"""
from constants import *
import numpy as np


# This function generates flattened boards of length n^2
# params:
#     prefix (str): accumulator varaible for tail recursion
#     numNodes (int): length of the flattened board
def generateFlatBoards(prefix, numNodes):
    if numNodes == 0:
        yield prefix
    else:
        for i in range(GENERATOR_SET_SIZE):
            newPrefix = prefix + GENERATOR_SET[i]
            yield from generateFlatBoards(newPrefix, numNodes - 1)


# This function runs generateFlatBoards and converts each generated string into n by n arrays
# params:
#     n (int): The dimensions of the board
def generateBoards(n):
    for flatBoard in generateFlatBoards("", n * n):
        board = [flatBoard[i * n:(i + 1) * n] for i in range((len(flatBoard) + n - 1) // n)]
        yield board


# Testing function
def main():
    for b in generateBoards(3):
        assert(all([len(row) == 3 for row in b]))
        print('\n'.join([''.join(['{:1}'.format(item) for item in row])
                         for row in b]))
        print("-----")


if __name__ == '__main__':
    main()
