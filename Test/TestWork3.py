import time


def has_cancelation(a, b, K):
    # todo: K for >1
    a_ = str(a)
    b_ = str(b)
    aa=set()
    for i in xrange(len(a_)-K+1):
        aa.add(a_[i:i+K])
    bb=set()
    for i in xrange(len(b_)-K+1):
        bb.add(b_[i:i+K])
    bb = set(list(b_))
    for x in aa:
        if x == "0" * K: continue
        for y in bb:
            if y == "0" * K: continue
            if x == y:
                for i in xrange(len(a_)-K+1):
                    if y == a_[i:i + K]:
                        sa = int(a_[:i] + a_[i + K:])
                        for j in xrange(len(b_)-K+1):
                            if y == b_[j:j + K]:
                                sb = int(b_[:j] + b_[j + K:])
                                try:
                                    if sa / float(sb) == a / float(b):
                                        return True
                                except ZeroDivisionError:
                                    continue
    return False


def test(N, K):
    xl = [0, 0]
    for x in xrange(11, 10**N-1):
        for y in xrange(x + 1, 10**N-1):
            if has_cancelation(x, y, K):
                xl[0] += x
                xl[1] += y
    print xl[0], xl[1]


if __name__ == "__main__":
    """
    2<=N<=4
    1<=K<=N-1
    """
    start = time.time()
    test(4,1)
    print "done", time.time() - start, "N,K=:", 3, 2
    """
    for N in xrange(2, 5):
        for K in xrange(1, N):
            start = time.time()
            test(N, K)
            print "done", time.time() - start, "N,K=:", N, K
    """