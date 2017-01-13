"""
Created on 28/11/2012

@author: mizzt
"""


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
    if n == 2: return 3

    res = n + 1
    aux = False
    while not aux:
        if isprime(res):
            aux = True
        else:
            res += 2
    return res


if __name__ == '__main__':
    N = 10001
    aux = 1
    for i in range(1, N + 1):
        aux = nextPrime(aux)

    print(aux)
