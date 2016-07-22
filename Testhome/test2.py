import math


def get_list_of_10000_primes():
    limit = 104729  # this is the 10000th prime
    if limit % 2 != 0:
        limit += 1
    primes_ = [True] * limit
    primes_[0], primes_[1] = [None] * 2
    for ind, val in enumerate(primes_):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes_[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
    return primes_


def get_all_primes_to_limit(limit):
    primes_ = []
    sieve_list = get_list_of_10000_primes()
    for i in xrange(limit + 1):
        if sieve_list[i]:
            primes_.append(i)
    return primes_


def get_distinct(n):
    res = (n - 1) ** 2
    xl = []
    total=0
    xls = set()
    for a in xrange(2,n+1):#int(math.ceil(math.sqrt(n)))+1):
        for e in xrange(1, n+1):#int(math.log(n) / math.log(a))+1):
            for b in xrange(2, n+1):
                if e*b>n or a**e>n: break
                val=a**(e*b)
                if val in xl:
                    print a,e*b, val,e
                    total+=1
                else:
                    xl.append(val)
    print res - total


def get_distinct2(n):
    xl = []
    for a in xrange(2, n + 1):
        for b in xrange(2, n + 1):
            if a**b in xl:
                #pass
                print a,b,a**b
            else:
                xl.append(a ** b)
    print len(xl)


n = input()
get_distinct2(n)
get_distinct(n)
