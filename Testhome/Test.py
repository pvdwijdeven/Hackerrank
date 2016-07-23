import sys
sys.setrecursionlimit(2000) # 10000

def pyth(n):
    def p(a, b, c):
        if n < a + b + c: return []
        return ([[a, b, c]] if a < b else [[b, a, c]]) \
             + p(a-b-b+c+c, a+a-b+c+c, a+a-b-b+c+c+c) \
             + p(a+b+b+c+c, a+a+b+c+c, a+a+b+b+c+c+c) \
             + p(c+c+b+b-a, c+c+b-a-a, c+c+c+b+b-a-a)
    return p(3, 4, 5)

pt= pyth(5000000)