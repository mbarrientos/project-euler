"""
Created on 03/12/2012

@author: mizzt
"""

from time import time


def isPerm(a, b):
    s1 = list(str(a))
    s2 = list(str(b))
    if len(s1) != len(s2): return False

    for x in s1:
        if x not in s2: return False
        s2[s2.index(x)] = ''

    return True


def metodo1():
    i = 1
    found = False
    while not found:
        if (isPerm(i, i * 2)
            and isPerm(i, i * 3)
            and isPerm(i, i * 4)
            and isPerm(i, i * 5)
            and isPerm(i, i * 6)):
            print(i)
            found = True

        # if i > 10**(floor(log10(i))+1)/6
        i += 1


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
