"""
Created on 25/11/2012

@author: mizzt
"""

from math import *
from time import time


def isPrime(n):
    """
    Check if integer n is a prime
    @return: bool
    """
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def nextPrime(n):
    res = n + 1
    aux = False
    while not aux:
        if isPrime(res):
            aux = True
        else:
            res += 1
    return res


if __name__ == '__main__':

    ini = time()

    N = 600851475143
    maxPrime = 1
    for i in range(1, int(ceil(sqrt(N)))):
        if (N % i == 0) & isPrime(i):
            maxPrime = i

    print(maxPrime)

    print("Tiempo: ", time() - ini, "sg")
