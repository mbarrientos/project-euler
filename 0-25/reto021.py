"""
Created on 04/12/2012

@author: mizzt
"""

from time import time


def d(n):
    return sum([i for i in range(1, n) if n % i == 0])


def amicable(a):
    b = d(a)
    return a != b and a == d(b)


def metodo1():
    A = []
    for i in range(1, 10000):
        if amicable(i) and d(i) < 10000:
            A += [i]
    print(A)
    print(sum(A))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
