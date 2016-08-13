# for big prime numbers:
import math


def conc(x, y):
    a = math.floor(math.log10(y))
    return int(x*10**(1+a)+y)


def sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return sieve


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    if n % 2 == 0: return False
    try:
       return slist[n]
    except IndexError:
       pass
    # if n in _known_primes or n in (0, 1):
    #     return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


slist = sieve(4000000)
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def create_sets():
    from time import time
    start = time()
    print ("starting...")
    K = 5
    N = 20000
    pl = primes(N)
    print (len(pl))
    myset = {}
    for i1 in range(0, len(pl)):
        p1 = pl[i1]
        myset[p1] = []
        for i2 in range(i1, len(pl)):
            p2 = pl[i2]
            if is_prime(conc(p1,p2)):
                if is_prime(conc(p2,p1)):
                    myset[p1].append(p2)
    print (time() - start)


def test():
    K = 5
    pl = primes(2000)
    for i1 in range(0, len(pl)):
        p1 = pl[i1]
        for i2 in range(i1, len(pl)):
            p2 = pl[i2]
            if is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1))):
                for i3 in range(i2, len(pl)):
                    p3 = pl[i3]
                    if is_prime(int(str(p1) + str(p3))) and is_prime(int(str(p3) + str(p1))) and is_prime(
                            int(str(p2) + str(p3))) and is_prime(int(str(p3) + str(p2))):
                        if K == 3:
                            print (p1 + p2 + p3, p1, p2, p3)
                        else:
                            for i4 in range(i3, len(pl)):
                                p4 = pl[i4]
                                if is_prime(int(str(p1) + str(p4))) and is_prime(int(str(p4) + str(p1))) and is_prime(
                                        int(str(p2) + str(p4))) and is_prime(int(str(p4) + str(p2))) and is_prime(
                                    int(str(p3) + str(p4))) and is_prime(int(str(p4) + str(p3))):
                                    if K == 4:
                                        print (p1 + p2 + p3 + p4, p1, p2, p3, p4)
                                    else:
                                        for i5 in range(i4, len(pl)):
                                            p5 = pl[i5]
                                            if is_prime(int(str(p1) + str(p5))) and is_prime(
                                                    int(str(p5) + str(p1))) and is_prime(
                                                int(str(p2) + str(p5))) and is_prime(
                                                int(str(p5) + str(p2))) and is_prime(
                                                int(str(p3) + str(p5))) and is_prime(
                                                int(str(p5) + str(p3))) and is_prime(
                                                int(str(p4) + str(p5))) and is_prime(int(str(p5) + str(p4))):
                                                if K == 5:
                                                    print (p1 + p2 + p3 + p4 + p5, p1, p2, p3, p4, p5)


create_sets()
