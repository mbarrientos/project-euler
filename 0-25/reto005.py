"""
Created on 26/11/2012

@author: mizzt
"""
from functools import reduce


def egcd(a, b):
    """
    Euclidean GCD

    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q  # use x//y for floor "floor division"
        b, a, x, y, u, v = a, r, u, v, m, n
    return b


def mcm(a, b):
    return (a * b) / egcd(a, b)


if __name__ == '__main__':
    print(reduce(mcm, range(1, 20)))
