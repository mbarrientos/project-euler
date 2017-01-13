"""
Created on 30/11/2012

@author: mizzt
"""

from math import ceil, sqrt
from time import time


def t(n):
    return n * (n + 1) / 2


def numFactores(n):
    cont = 0
    for i in range(1, int(ceil(sqrt(n)))):
        if n % i == 0:
            cont += 1

    return 2 * cont


def metodo1():
    n = 1
    while numFactores(t(n)) <= 500:
        n += 1
    print(n, ": ", t(n))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
