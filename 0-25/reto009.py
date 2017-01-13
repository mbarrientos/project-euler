"""
Created on 28/11/2012

@author: mizzt
"""
from math import sqrt, floor
from time import time


def pitagoras(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


if __name__ == '__main__':
    ini = time()

    res = [a * b * sqrt(a ** 2 + b ** 2)
           for a in range(1, 1000)
           for b in range(1, 1000)
           if a < b and
           (floor(sqrt(a ** 2 + b ** 2)) == sqrt(a ** 2 + b ** 2)) and
           (a + b + sqrt(a ** 2 + b ** 2) == 1000)]

    print(res)
    print("Tiempo: ", time() - ini, "sg")
