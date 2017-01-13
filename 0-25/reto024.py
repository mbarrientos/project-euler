"""
Created on 04/12/2012

@author: mizzt
"""

from time import time


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def metodo1(N):
    sol = []
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = N
    for i in range(len(digits), 0, -1):
        fi = factorial(i - 1)
        ni = n / fi
        sol.append(digits[ni])
        digits = digits[:ni] + digits[ni + 1:]
        n = n % fi
        print("S=", sol, ", D=", digits)

    sum = 0
    for i in range(0, 10):
        sum += sol[10 - i - 1] * 10 ** i
    print(sum)


"""
1000000th permutation of 0,1,2,3,4,5,6,7,8,9 ->
274240th permutation of 0,1,3,4,5,6,7,8,9 ->
32320th permutation of 0,1,3,4,5,6,8,9 ->
"""

if __name__ == '__main__':
    N = 999999
    ini = time()
    metodo1(N)
    print("Tiempo: ", time() - ini, "sg")
