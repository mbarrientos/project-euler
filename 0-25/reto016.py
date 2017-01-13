"""
Created on 03/12/2012

@author: mizzt
"""

from math import log10, ceil, floor
from time import time


def metodo1(N):
    n = 2 ** N
    suma = 0
    print("2^N = ", n)
    print("NDigitos = ", int(ceil(log10(n))) + 1)
    for i in range(1, int(ceil(log10(n))) + 1):
        digit = floor(n / (10 ** (i - 1))) % 10
        # print(digit)
        suma += digit
    print(suma)


def metodo2(N):
    print(sum([int(i) for i in str(2 ** N)]))


if __name__ == '__main__':
    N = 1000
    ini = time()
    metodo2(N)
    print("Tiempo: ", time() - ini, "sg")
