"""
Created on 28/11/2012

@author: mizzt
"""

from math import ceil, sqrt
from time import time


def isprime(n):
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
    """
    Look for the next prime greater than n, given n prime
    @return: int
    """
    if n == 1: return 2
    if n == 2: return 3
    if n == 3: return 5

    aux = False
    while not aux:
        if n % 10 == 3:
            n += 4
        else:
            n += 2

        if isprime(n):
            aux = True

    return n


def metodo1(N):
    n = 2
    sum = 0

    while n < N:
        sum += n
        n = nextPrime(n)

    print(sum)


def metodo2(N):
    """
    Metodo usando la criba de Erastotenes
    """

    criba = [True for i in range(0, N)]
    criba[0] = False
    criba[1] = False

    limit = int(ceil(sqrt(N)))

    for i in range(1, limit):
        if criba[i]:
            for n in range(i * i, len(criba), i):
                criba[n] = False

    print(sum([x for x in range(0, N) if criba[x]]))


if __name__ == '__main__':
    N = 2000000
    ini = time()
    metodo2(N)
    print("Tiempo: ", time() - ini, "sg")
