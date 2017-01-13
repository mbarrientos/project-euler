"""
Created on 08/11/2012

@author: Carlitos
"""
from math import floor, ceil, sqrt
from time import time


# def criba_eratostenes(n):
#    multiplos = set()
#    res = []
#    for i in range(2, n+1):
#        if i not in multiplos:
#            res.append(i)
#            multiplos.update(range(i*i, n+1, i))
#    return res

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


def nextPrime(n):
    res = n + 1
    aux = False
    while not aux:
        if isprime(res):
            aux = True
        else:
            res += 1
    return res


def factorial(elem):
    res = 1
    for i in range(1, elem + 1):
        res *= i
    return res


def calculaFuncion2(p):
    res = 0
    for i in range(1, 6):
        res += factorial(p - i)
    return res % p


def calculaFuncion3(p):
    aux = factorial(p - 5)
    sum = 0
    for i in range(4, 0, -1):
        sum += aux % p
        aux *= (p - i)
    sum += aux % p
    return sum % p


def euclid(a, b):
    """
    The extended Euclidean algorithm.
    Arguments: two integers a and b.
    Returns: The tuple (x, y, gcd(a, b))
        where x and y satisfy the equation ax + by = gcd(a, b)
    """
    x = 0
    lastx = 1
    y = 1
    lasty = 0

    while b != 0:
        # This must be integer devision; floor required in Python 3.
        quotient = floor(a / b)

        # Hooray for tuple assignment!
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - quotient * x, x)
        (y, lasty) = (lasty - quotient * y, y)
    return lastx, lasty, a


def calculaFuncion4(p):
    return (modinv(p - 24, p) + modinv(p + 6, p) + modinv(p - 2, p)) % p


# def invmodp(a, p):
#    '''
#    The multiplicitive inverse of a in the integers modulo p.
#    Return b s.t.
#    a * b == 1 mod p
#    '''
#    r = a
#    d = 1
#    for count in xrange(p):
#        d = ((p // r + 1) * d) % p
#        r = (d * a) % p
#        if r == 1:
#            break
#    else:
#        raise ValueError('%d has no inverse mod %d' % (a, p))
#    return d

def factorialMod(n, modulus):
    ans = 1
    if n <= modulus // 2:
        # calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1, n + 1):
            ans = (ans * i) % modulus
    else:
        # Fancypants method for large n
        for i in range(1, modulus - n):
            ans = (ans * i) % modulus
        ans = modinv(ans, modulus)

        # Since m is an odd-prime, (-1)^(m-n) = -1 if n is even, +1 if n is odd
        if n % 2 == 0:
            ans = -1 * ans + modulus
    return ans % modulus


def calculaFuncion5(p):
    return (factorialMod(p - 5, p) + factorialMod(p - 4, p) + factorialMod(p - 3, p)) % p


def calculaFuncion6(p):
    return (inv_mult(p - 24, p) + inv_mult(p + 6, p) + inv_mult(p - 2, p)) % p


# Iterative Algorithm (xgcd)
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q  # use x//y for floor "floor division"
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m


def calculaFuncion(p):
    aux = factorial(p - 5)
    sum = 0
    for i in range(4, 0, -1):
        sum += aux
        aux *= (p - i)
    sum += aux
    return sum % p


def mcd(n, m):
    m_aux = n % m
    if m_aux == 0:
        return m
    elif m_aux == 1:
        return 1
    else:
        return mcd(m, m_aux)


def inv_mult(a, n):
    #    if(mcd(a, n) != 1):
    #        print(str(a) + " NO TIENE INVERSO MULTIPLICATIVO EN " + str(n))
    #    else:
    #        for i in range(1, n) :
    #            if((a * i - 1) % n == 0):
    #                return i
    for i in range(1, n):
        if (a * i - 1) % n == 0:
            return i


# def calculaFuncion7(p):
#    return ((p-3)*reciprocalMod(8%p,p)%p)

def reciprocalMod(x, m):
    if m < 0 or x < 0 or x >= m:
        return None
    y = x
    x = m
    a = 0
    b = 1
    while y != 0:
        z = x % y
        c = a - x / y * b
        x = y
        y = z
        a = b
        b = c
    if x == 1:
        return a % m
    else:
        return None


def calculaFuncion8(p):
    menostres = modinv(p - 2, p) % p
    menoscuatro = (menostres * modinv(p - 3, p)) % p
    menoscinco = (menoscuatro * modinv(p - 4, p)) % p

    return (menostres + menoscuatro + menoscinco) % p


def calculaFuncion9(p):
    return (modinv(p - 24, p) + modinv(p + 6, p) + modinv(p - 2, p)) % p


def metodo1():
    print("Comienza...")
    ini = time()

    i = 5
    fin = False
    aux = None
    sum = 0
    printlimit = i
    while not fin:
        aux = nextPrime(i)
        if aux >= 100:
            fin = True
        else:
            sum += calculaFuncion9(aux)
            i = aux

    print("Suma:", sum, "en", time() - ini, "sg")


if __name__ == '__main__':

    print("Comienza...")
    ini = time()

    # print(calculaFuncion8(7))

    N = 30000000
    criba = [True for i in range(0, N)]
    criba[0] = False
    criba[1] = False

    limit = int(ceil(sqrt(N)))

    for i in range(1, limit):
        if criba[i]:
            for n in range(i * i, len(criba), i):
                criba[n] = False

    print(480 + sum([calculaFuncion9(x) for x in range(100, N) if criba[x]]))

    # metodo1()
    print("Tiempo: ", time() - ini, "sg")
