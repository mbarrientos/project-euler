"""
Created on 23/11/2012

@author: mizzt
"""

from math import floor
from time import time


def mul3(n):
    ans = list()
    for i in range(1, int(floor((n - 1) / 3)) + 1):
        ans.append(i * 3)

    return ans


def mul5no3(n):
    ans = list()
    for i in range(1, int(floor((n - 1) / 5)) + 1):
        m = 5 * i
        if m % 3 != 0:
            ans.append(m)

    return ans


def metodo1(n):
    return sum(mul3(n)) + sum(mul5no3(n))


def metodo2(n):
    sum3 = 3 * (int(floor((n - 1) / 3)) + 1) * int(floor((n - 1) / 3)) / 2
    sum5 = 5 * (int(floor((n - 1) / 5)) + 1) * int(floor((n - 1) / 5)) / 2
    sum15 = 15 * (int(floor((n - 1) / 15)) + 1) * int(floor((n - 1) / 15)) / 2

    return sum3 + sum5 - sum15


if __name__ == '__main__':
    print("Comienza...")

    n = 1000

    ini = time()
    print("Suma: ", metodo2(n))
    print("Tiempo: ", time() - ini, "sg")
