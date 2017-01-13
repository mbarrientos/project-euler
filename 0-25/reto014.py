"""
Created on 03/12/2012

@author: mizzt
"""

from time import time


def nextSeq(i):
    if i % 2 == 0:  # even
        return i // 2
    else:
        return i * 3 + 1


def recSeq(s, i):
    next = nextSeq(i)
    if not next in s:
        s[next] = recSeq(s, next)
        return s[next] + 1
    return s[next] + 1


def metodo1(N):
    # s = [0 for i in range (0,N)]
    s = dict()

    s[1] = 1
    for i in range(2, N):
        s[i] = recSeq(s, i)
        # print("i=",i," - s[",i,"]=",s[i] )

    maxRes = 1
    for i in range(1, N):
        if s[i] > s[maxRes]:
            maxRes = i

    print(maxRes)
    print(max([i for i in s.keys()]))


if __name__ == '__main__':
    N = 1000000
    ini = time()
    metodo1(N)
    # prueba(N)
    print("Tiempo: ", time() - ini, "sg")
