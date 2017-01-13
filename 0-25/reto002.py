"""
Created on 25/11/2012

@author: mizzt
"""

from time import time


def fibonacci(n):
    x1, x2 = 0, 1
    print(x1)
    print(x2)
    for i in range(1, n):
        print(x1 + x2)
        x2 += x1
        x1 = x2 - x1


def fibonacciPares(n):
    x1, x2 = 0, 1
    print(x1)
    for i in range(3, n):
        if i % 3 == 1:
            print(x1 + x2)
        x2 += x1
        x1 = x2 - x1


def sumFibonacci(lim):
    x1, x2 = 0, 1
    while x2 < lim:
        x2 += x1
        x1 = x2 - x1


if __name__ == '__main__':

    ini = time()

    lim = 4000000
    x1, x2 = 0, 1
    i = 3
    suma = 0

    while x2 < lim:
        i += 1
        x2 += x1
        x1 = x2 - x1
        if i % 3 == 2:
            suma += x2

    print("Tiempo: ", time() - ini, "sg")

    print(suma)
