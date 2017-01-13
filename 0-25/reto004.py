"""
Created on 26/11/2012

@author: mizzt
"""


def esPalindromo(n):
    mstr = str(n)
    if mstr == mstr[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(max([i * j for i in range(100, 1000) for j in range(100, 1000) if (esPalindromo(i * j))]))
