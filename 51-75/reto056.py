"""
Created on 04/12/2012

@author: mizzt
"""

from time import time


def sumDigitos(n):
    return sum([int(i) for i in str(n)])


def metodo1():
    maxSum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            aux = sumDigitos(a ** b)
            if maxSum < aux:
                maxSum = aux

    print(maxSum)


if __name__ == '__main__':
    ini = time()
    print(sumDigitos('0000000000000001'))
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
