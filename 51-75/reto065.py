from __future__ import division

'''
Created on 05/12/2012

@author: mizzt
'''
from fractions import *
from time import time
from math import ceil


def suc(i, n):
    k = 1
    if i % 3 == 2:
        k = int(ceil(i / 3)) * 2
    if i == n:
        return k
    else:
        return k + (1 / suc(i + 1, n))


def metodo1():
    t = 1
    print(sum([int(i) for i in str(Fraction.from_float(1 + (suc(0, 100))).numerator)]))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
