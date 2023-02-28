"""
Per the problem statement, there are 3 qualifications for a board to be valid:
    1) Starting from any non-empty space (i.e. any boat), you can walk to every other non-empty space (Walkable)
    2) No boat can be facing another boat
    3) Each boat must have a path from its position to the edge of the board AND the first move in this
       path must be the in the direction it was originally facing (Unpackable)
"""
from constants import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Check if a board is a valid configuration
def isValidConfiguration(board):
    return checkIsWalkable(board) and checkIsUnpackable(board)


# Checks if the board is walkable by converting it to a graph and then
# checking if the graph is fully connected
def checkIsWalkable(board):
    boardGraph = toUndirectedGraph(board)
    return nx.is_connected(boardGraph)


def checkIsUnpackable(board):
    print(board)
    r, c = board.shape
    edgeBoard = np.full((r + 2, c + 2), EDGE)

    _, k = edgeBoard.shape
    edgeBoard[1:k - 1, 1:k - 1] = board
    print(edgeBoard)
    return


# Converts board to an adjacency matrix and then an undirected graph
def toUndirectedGraph(board):
    # Convert board to binary matrix where 0s are open spaces and 1s are boats
    original_shape = board.shape
    board = np.where(board != OPEN, 1, 0).reshape(original_shape)

    # Convert all ones to unique values
    u = 1
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == 1:
                board[i, j] = u
                u += 1

    print(board)
    print(board.shape)
    boardAdjMat = createAdjMat(board)
    graph = nx.from_numpy_array(boardAdjMat)
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos)
    plt.show()

    return graph


# Function to create an adjacency matrix from a 2D numpy array where all nodes are represented by
# unique, positive integers.
def createAdjMat(X):
    nodeIndex = np.transpose(X.nonzero())
    print(nodeIndex)
    nodeCount = len(nodeIndex)

    mat = np.zeros((nodeCount, nodeCount))
    for idx in nodeIndex:
        for adjIdx in getOffsetIndices(idx, X.shape[0]):
            if adjIdx in nodeIndex:
                mat[X[idx[0], idx[1]] - 1, X[adjIdx[0], adjIdx[1]] - 1] = 1

    return mat


def getOffsetIndices(idx, dim):
    x, y = idx[0], idx[1]
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dimRange = range(dim)
    adjs = []
    for dx, dy in offsets:
        if (x + dx in dimRange) and (y + dy in dimRange):
            adjs.append([x + dx, y + dy])

    return adjs


def main():
    checkIsUnpackable(np.asarray([[NORTH, NORTH, NORTH, NORTH],
                                  [WEST, OPEN, OPEN, EAST],
                                  [WEST, OPEN, OPEN, EAST],
                                  [SOUTH, SOUTH, SOUTH, SOUTH]]))

    # print("Board {} walkable".format("is" if result else "is not"))


if __name__ == '__main__':
    main()
