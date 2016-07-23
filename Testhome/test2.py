import sys
sys.setrecursionlimit(2000) # 10000

def pyth(n):
    def p(a, b, c):
        if n < a + b + c: return []
        return ([[a, b, c,a+b+c]] if a < b else [[b, a, c,a+b+c]]) \
             + p(a-b-b+c+c, a+a-b+c+c, a+a-b-b+c+c+c) \
             + p(a+b+b+c+c, a+a+b+c+c, a+a+b+b+c+c+c) \
             + p(c+c+b+b-a, c+c+b-a-a, c+c+c+b+b-a-a)
    return p(3, 4, 5)

if __name__ == '__main__':
    import sys
    pt=[]
    for x in pyth(5000000):
        pt.append(x)

    pl=[0 for x in xrange(5000000)]
    for x in pt:
        i=1
        while x[3]*i<5000000:
            pl[x[3]*i]+=1
            i+=1
    ppp=[]
    maxx=0
    maxi=0
    for i,x in enumerate(pl):
        if x>maxx:
            maxx=x
            maxi=i
        ppp.append(maxi)
    for _ in xrange(input()):
        N=input()
        print ppp[N]