# -*- coding: utf-8 -*-

"""
Matrix Layer Rotation

Hackerrank - Algorithms - Implementation

Author: PvdWijdeven
"""

#########################
# Enable/disable debug: #
# 0= no debug           #
# 1= debug unrolling    #
# 2= debug rolling      #
# 4= debug rotation     #
#########################

debug = 7


def getinput():
    if debug:
        # caseT1: (ordered matrix):
        # m, n, r = 5, 4, 7
        # mymatrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
        # caseT2: (ordered matrix):
        # m, n, r = 2, 8, 8
        # mymatrix = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
        # case0:
        m, n, r = 4, 4, 1
        mymatrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        # case1:
        # m, n, r = 5, 4, 7
        # mymatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        # case2:
        # m, n, r = 5, 4, 7
        # mymatrix = [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16], [19, 20, 21, 22], [25, 26, 27, 28]]
        # case3:
        # m, n, r = 2, 2, 3
        # mymatrix = [[1, 1], [1,1]]
    else:
        mymatrix = []
        m, n, r = map(int, raw_input().split())
        for _ in xrange(m):
            mymatrix.append(map(int, raw_input().split()))
    return m, n, r, mymatrix


def unrollmatrix(mm):
    um = []
    if debug & 1: print"\n***unrollmatrix***"
    for i in xrange(0, min(N, M) / 2):
        cur_um = []
        # left column
        for r in xrange(i, M - i):
            if debug & 1: print "left column:", r, i
            cur_um.append(mm[r][i])
        # lower row
        for c in xrange(i + 1, N - i-1):
            if debug & 1: print "lower row:", M - i - 1, c
            cur_um.append(mm[M - i - 1][c])
        # right column
        for r in xrange(M - i-1, i-1, -1):
            if debug & 1: print "right column:", r, N - i-1
            cur_um.append(mm[r][N - i-1])
        # upper row
        for c in xrange(N - i - 2, i, -1):
            if debug & 1: print "upper row:", i, c
            cur_um.append(mm[i][c])
        um.append(cur_um)
    return um


def rollupmatrix(mlist):
    if debug & 2: print"\n***rollupmatrix***"
    localmatrix = [[0 for i in range(N)] for j in range(M)]
    for i in xrange(0, min(N, M) / 2):
        j = 0
        # left column
        for r in xrange(i, M - i):
            if debug & 2: print "left column:", r, i, mlist[i][j]
            localmatrix[r][i] = mlist[i][j]
            j += 1
        # lower row
        for c in xrange(i + 1, N - i - 1):
            if debug & 2: print "lower row:", M - i-1, c
            localmatrix[M- i-1][c] = mlist[i][j]
            j += 1
        # right column
        for r in xrange(M - i - 1, i, -1):
            if debug & 2: print "right column:", r, N - i - 1
            localmatrix[r][N - i - 1] = mlist[i][j]
            j += 1
        # upper row
        for c in xrange(N - i - 1, i, -1):
            if debug & 2: print "upper row:", i, c
            localmatrix[i][c] = mlist[i][j]
            j += 1
    return localmatrix


def rotatematrix(mlist, rotations):
    if debug & 4: print"\n***rotatematrix***"
    for i in xrange(len(mlist)):
        x = list(mlist[i])
        for j in xrange(rotations % len(x)):
            if debug & 4:
                print "before rotate:", x
            x = [x.pop()] + x
            if debug & 4:
                print "after rotate:", x
        mlist[i] = list(x)
    return mlist


# get input
M, N, R, matrix = getinput()

# roll out matrix
unr = unrollmatrix(matrix)

# rotate matrix elements
rot = rotatematrix(unr, R)

# roll back into matrix
rol = rollupmatrix(unr)

# print result
for x in rol:
    for y in x:
        print y,
    print
