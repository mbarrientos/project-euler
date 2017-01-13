"""
Created on 04/12/2012

@author: mizzt
"""

from time import time


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sumDigitos(n):
    return sum([int(i) for i in str(n)])


def metodo1():
    print(sumDigitos(factorial(100)))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
