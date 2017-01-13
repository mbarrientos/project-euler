from __future__ import division

'''
Created on 29/11/2012

@author: mizzt
'''

from time import time


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


def test(x, y):
    x1, x2 = x // 10, x % 10
    y1, y2 = y // 10, y % 10

    # print(x1,x2, '-', x, x1/x2)
    # print(y1,y2, '-', y)
    c = 0
    d = 0

    if x1 == y1:
        c = x2
        d = y2
    else:
        if x1 == y2:
            c = x2
            d = y1
        else:
            if x2 == y1:
                c = x1
                d = y2
            else:
                if x2 == y2:
                    c = x1
                    d = y1
                else:
                    return False

    if (x / y) == (c / d):
        print((x, y), "<--", x / y, c / d, "-->", (c, d))

        return c, d
    else:
        return False


def reduceLista(l):
    x, y = 1, 1
    for (a, b) in l:
        x *= a
        y *= b

    return y / egcd(x, y)


def metodo1():
    sol = [test(x, y) for x in range(11, 100) for y in range(11, 100) if (x < y and (x % 10 != 0) and (y % 10 != 0))]
    sol = [e for e in sol if e != False]
    print(sol)
    print(reduceLista(sol))


def metodo2():
    denproduct = 1
    nomproduct = 1
    for i in range(1, 10):
        for den in range(1, 10):
            for nom in range(1, 10):
                if nom < den < i:
                    if (nom * 10 + i) * den == nom * (i * 10 + den):
                        print(nom, '/', den)
                        denproduct *= den
                        nomproduct *= nom

    print(denproduct / egcd(denproduct, nomproduct))


if __name__ == '__main__':
    ini = time()
    metodo1()
    metodo2()
    print("Tiempo: ", time() - ini, "sg")
