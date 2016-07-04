debug = True

if debug:
    import time

    start = time.time()
    T = 10
    Nlist = [10, 15, 20, 5 * 10 ** 6, 10 ** 5, 10 ** 6, 1000, 999, 8, 3]
else:
    Nlist = []
    T = input()
    for i in range(T):
        Nlist.append(input())

limit = max(Nlist) + 1
collatz_length = [0] * limit
collatz_length[1] = 1

for i in range(1, limit):
    n, s = i, 0
    TO_ADD = []  # collatz_length not yet known
    while n > limit - 1 or collatz_length[n] < 1:
        TO_ADD.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        s += 1
    # collatz_length now known from previous calculations
    p = collatz_length[n]
    for j in range(s):
        m = TO_ADD[j]
        if m < limit:
            new_length = collatz_length[n] + s - j
            collatz_length[m] = new_length
maxfound = 0
maxi = 0
maxList = []
for i in range(max(Nlist) + 1):
    if maxfound <= collatz_length[i]:
        maxfound = collatz_length[i]
        maxi = i
    maxList.append(maxi)

for x in Nlist:
    print maxList[x]

if debug:
    elapsed = (time.time() - start)
    print "found in %s seconds" % elapsed
