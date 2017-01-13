"""
Created on 28/11/2012

@author: mizzt
"""


def sumaCuadrados(N):
    suma = 0
    for i in range(1, N + 1):
        suma += i ** 2
    return suma


def cuadradoSuma(N):
    suma = N * (N + 1) / 2
    return suma ** 2


if __name__ == '__main__':
    N = 1000
    print(abs(sumaCuadrados(N) - cuadradoSuma(N)))
