"""
Created on 05/12/2012

@author: mizzt
"""

from math import log10
from time import time


def metodo1():
    i1 = 1
    i2 = 1
    i = 2
    found = False
    while not found:
        i3 = i1 + i2
        i1 = i2
        i2 = i3
        i += 1
        if log10(i2) >= 999:
            print(i)
            found = True


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
