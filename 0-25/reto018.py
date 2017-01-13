"""
Created on 03/12/2012

@author: mizzt
"""

from time import time


def parse_input():
    f = open('input018', 'r')
    return [map(int, j.split()) for j in [i for i in f.read().split("\n")]]


def metodo1():
    T = parse_input()
    print(maxBranch(T, 0, 0))


def maxBranch(T, i, j):
    if i >= len(T) or j >= len(T[i]): return 0
    left_sum = maxBranch(T, i + 1, j)
    right_sum = maxBranch(T, i + 1, j + 1)
    if left_sum > right_sum:
        tail = left_sum
    else:
        tail = right_sum
    return T[i][j] + tail


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
