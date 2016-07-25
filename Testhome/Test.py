def check_perms(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    prime_list_ = [2] + [i for i in xrange(3, n, 2) if sieve[i]]
    return prime_list_[168:], sieve


n, k = map(int, raw_input().split())
prime_list, sieve_list = primes(1000000)


def is_prime(number):
    try:
        x = number == 2 or (sieve_list[number] and number % 2 != 0)
    except IndexError:
        print number
        raise IndexError
    return x


def k3():
    my_primes = [[] for x in xrange(0, 7)]
    for x in prime_list:
        my_primes[len(str(x))].append(x)
    sum = 0
    for x in xrange(4, 7):
        for i, p in enumerate(my_primes[x]):
            if p > n: break
            if p > 10 ** x / k:
                break
            for j in my_primes[x][i + 1:]:
                if j + j - p < ((10 ** x)):
                    if is_prime(j + j - p):
                        if not check_perms(j, p): continue
                        if check_perms(j + j - p, p):
                            sum += 1
                            print str(p) + str(j) + str(j + (j - p))
                else:
                    break


def k4():
    my_primes = [[] for x in xrange(0, 7)]
    for x in prime_list:
        my_primes[len(str(x))].append(x)
    for x in xrange(4, 7):
        for i, p in enumerate(my_primes[x]):
            if p > n: break
            if p > 10 ** x / k:
                break
            for j in my_primes[x][i + 1:]:
                if j + (j - p)+(j-p) < ((10 ** x)):
                    if is_prime(j + j - p):
                        if not check_perms(j, p): continue
                        if check_perms(j + j - p, p):
                            if is_prime(j + (j - p) + (j - p)):
                                if check_perms(p, j + (j - p) + (j - p)):
                                    print str(p) + str(j) + str(j + (j - p)) + str(j + (j - p) + (j - p))
                else:
                    break


if k == 3:
    k3()
else:
    k4()
