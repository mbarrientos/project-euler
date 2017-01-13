"""
Created on 04/12/2012

@author: mizzt
"""

from time import time


def parseInput():
    f = open("input022", 'r')
    return f.read()[1:-1].split("\",\"")


def score(name):
    return sum([ord(c) - 64 for c in name])


def metodo1():
    L = parseInput()
    L.sort()
    print(sum([score(L[i]) * (i + 1) for i in range(0, len(L))]))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
