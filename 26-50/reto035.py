"""
Created on 07/11/2012

@author: Carlitos
"""
from functools import reduce
from itertools import product
from time import time


def rotate(n):
    """
    Rota un numero.
    @return: int
    """
    m = 1
    while n / m > 10:
        m *= 10
    return (m * (n % 10)) + n / 10


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


def esPrimoCircular(elem, candidatos):
    """
    Chequea si el numero es primo circular.
    """
    res = True
    res = res and isprime(elem)
    aux = str(elem)
    for _ in range(len(aux)):
        aux = rotate(int(aux))
        res = res and isprime(rotate(aux)) and (rotate(aux) in candidatos)
    return res


def generarCandidatos():
    """
    Genera los candidatos a ser numeros primos circulares.
    @return: list(int)
    """
    res = [1, 2, 3, 5, 7]
    for i in range(2, 7):
        res.extend([reduce(lambda x, y: int(x) * 10 + int(y), n) for n in product("1379", repeat=i)])
    return res


# =====================
#       MAIN
# =====================
if __name__ == '__main__':
    inicio = time()
    candidatos = generarCandidatos()
    res = 0
    for elem in candidatos:
        if esPrimoCircular(elem, candidatos):
            res += 1
    print(time() - inicio, "sg")
    print(res)
