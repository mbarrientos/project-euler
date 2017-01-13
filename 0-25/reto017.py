"""
Created on 03/12/2012

@author: mizzt
"""

from time import time


def metodo1():
    s1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n1 = list(map(len, s1))  # [0,3,3,5,4,4,3,5,5,4]
    s10 = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    n10 = list(map(len, s10))  # [0,3,6,6,6,5,5,7,6,6]
    sIrreg = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen']
    nirreg = list(map(len, sIrreg))

    sum = 0
    for i2 in range(0, 10):
        for i1 in range(0, 10):
            for i0 in range(0, 10):
                if i2 != 0:
                    sum += n1[i2] + len("hundred")
                    print(s1[i2], 'hundred')

                if i1 != 0:
                    if i2 != 0:
                        sum += len("and")
                        print('and')
                    if i1 == 1:
                        sum += nirreg[i0]
                        print(sIrreg[i0])
                    else:
                        sum += n10[i1]
                        print(s10[i1])

                if i0 != 0 and i1 != 1:
                    if i2 != 0 and i1 == 0:
                        sum += len("and")
                        print('and')
                    sum += n1[i0]
                    print(s1[i0])
                print('')

    print(sum + len("onethousand"))


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
