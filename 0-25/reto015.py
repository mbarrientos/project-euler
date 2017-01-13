"""
Created on 03/12/2012

@author: mizzt
"""

from time import time


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def metodo1(N):
    fn = factorial(N)
    print(factorial(2 * N) / (fn ** 2))


if __name__ == '__main__':
    N = 80
    ini = time()
    metodo1(N)
    print("Tiempo: ", time() - ini, "sg")
