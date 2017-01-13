"""
Created on 28/11/2012

@author: mizzt
"""
from time import time


# 1000000000 < N < 3300000000

def test(N):
    s = str(N)
    for i in range(0, 10):
        if s[i * 2] != str((i + 1) % 10):
            return False

    return True


if __name__ == '__main__':

    ini = time()

    found = False
    i = 1000000030
    while not found:
        if test(i ** 2):
            print(i)
            found = True

        if i % 100 == 30:
            i += 40
        else:
            i += 60

    print("Tiempo: ", time() - ini, "sg")
