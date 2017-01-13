"""
Created on 30/11/2012

@author: mizzt
"""

from time import time


def parseInput():
    f = open('input013', 'r')
    return map(int, f.read().split())


def metodo1():
    L = parseInput()
    print(L)

    print(sum(L))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
