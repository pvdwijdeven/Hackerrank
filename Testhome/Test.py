import math

def test():
    K = 2
    n=7
    d1 = n * (3 * n - 1) / 2 - (n - K) * (3 * (n - K) - 1) / 2
    d2 = n * (3 * n - 1) / 2 + (n - K) * (3 * (n - K) - 1) / 2
    print d1
    print d2
    # 3x^2-x-2d=0
    # 1 + math.sqrt(1-4*3*-2*d1)/6
    try:
        x1 = 1 + math.sqrt(1 - 4 * 3 * -2 * d1) / 6.0
    except ValueError:
        x1=-1
    try:
        x2 = 1 - math.sqrt(1 - 4 * 3 * -2 * d1) / 6.0
    except ValueError:
        x2=-1
    try:
        x3 = 1 + math.sqrt(1 - 4 * 3 * -2 * d2) / 6.0
    except ValueError:
        x3=-1
    try:
        x4 = 1 - math.sqrt(1 - 4 * 3 * -2 * d2) / 6.0
    except ValueError:
        x4=-1
    print x1,x2,x3,x4

test()