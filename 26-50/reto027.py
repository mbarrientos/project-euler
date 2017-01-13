"""
Created on 05/12/2012

@author: mizzt
"""

'''
Considering quadratics of the form:

n^2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, 
for the quadratic expression that produces the 
maximum number of primes for consecutive values of n, starting with n = 0.
'''

from time import time


def isPrime(n):
    n = abs(n)
    if n == 0: return False
    if n == 1: return True
    i = 2
    while n % i != 0:
        if i >= n - 1:
            return True
        i += 1
    return False


def numPrimes(a, b):
    n = 0
    while isPrime(n ** 2 + a * n + b):
        n += 1
    return n - 1


def metodo1(N):
    # print(isPrime(6), isPrime(7))
    # print(max([(numPrimes(a,b),a,b) for a in range(-1000,1000) for b in range(-1000,1000) if numPrimes(a,b)>40]))
    # print([(n**2 -61*n + 971) for n in range(0,70)])
    # print([isPrime(n**2 -61*n + 971) for n in range(0,75)])
    print(-61 * 971)


if __name__ == '__main__':
    ini = time()
    metodo1(1000)
    print("Tiempo: ", time() - ini, "sg")
