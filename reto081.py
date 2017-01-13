"""
Created on 12/12/2012

@author: mizzt
"""
'''
RETO 81 - 
Find the minimal path sum, in matrix.txt, 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
'''
from time import time


def parseInput():
    f = open('input081', 'r')
    filas = [j for j in f.read().split("\n")]
    return [map(int, i.split(',')) for i in filas]


def minSum(ab, ij, M):
    a, b = ab
    i, j = ij
    if (a, b) == (i, j): return M[a][b]
    if i == a:
        return minSum((a, b), (i, j - 1), M) + M[i][j]
    if j == b:
        return minSum((a, b), (i - 1, j), M) + M[i][j]
    return min(minSum((a, b), (i, j - 1), M), minSum((a, b), (i - 1, j - 1), M), minSum((a, b), (i - 1, j), M)) + M[i][
        j]


def metodo1():
    M = parseInput()

    print("TOTAL:", minSum((0, 0), (10, 10), M))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
