from itertools import permutations, combinations

from math import sqrt


def prime(n):
    if n == 1 or n == 2:
        return True
    elif n > 2:
        for i in range(3, int(sqrt(n)) + 1):
            if n % (i + 1) == 0:
                return False
        return True


def primes(max):
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2
    while q <= max:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def primeset(*args):
    return all([prime(int(''.join(i))) for i in permutations([str(i) for i in args], 2)])


N = 100
sets = []
for set_size in range(1, 6):
    sets.extend([i for i in combinations([p for p in primes(N)], set_size) if primeset(*i)])
