# -*- coding: utf-8 -*-

"""
Matrix Layer Rotation

Hackerrank - Algorithms - Implementation

Author: PvdWijdeven
"""


#########################
#Enable/disable debug:  #
# 0= no debug           #
# 1= debug unrolling    #
# 2= debug rolling      #
# 4= debug rotation     #
#########################

debug = 3


def getinput():
    if debug:
        m, n, r = 5, 4, 7
        # mymatrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
        mymatrix = [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16], [19, 20, 21, 22], [25, 26, 27, 28]]
    else:
        mymatrix = []
        m, n, r = map(int, raw_input().split())
        for _ in xrange(M):
            matrix.append(map(int, raw_input().split()))
    return m, n, r, mymatrix


def unrollmatrix(mm):
    um = []
    if debug&1: print"\n***unrollmatrix***"
    for i in xrange(0, min(N, M) / 2):
        cur_um = []
        # left column
        for r in xrange(i, N + 1 - i):
            if debug&1: print "left column:", r, i
            cur_um.append(mm[r][i])
        # lower row
        for c in xrange(i + 1, M - i - 1):
            if debug&1: print "lower row:", N - i, c
            cur_um.append(mm[N - i][c])
        # right column
        for r in xrange(N - i - 1, i, -1):
            if debug&1: print "right column:", r, M - i - 2
            cur_um.append(mm[r][M - i - 2])
        # upper row
        for c in xrange(M - i - 2, i, -1):
            if debug&1: print "upper row:", i, c
            cur_um.append(mm[i][c])
        um.append(cur_um)
    return um


def rollupmatrix(mlist):
    if debug & 2: print"\n***rollupmatrix***"
    localmatrix = [[0 for i in range(N)] for j in range(M)]
    for i in xrange(0, min(N, M) / 2):
        # left column
        j = 0
        for r in xrange(i, N + 1 - i):
            if debug&2: print "left column:", r, i, mlist[i][j]
            localmatrix[r][i] = mlist[i][j]
            j += 1
        # lower row
        for c in xrange(i + 1, M - i - 1):
            if debug&2: print "lower row:", N - i, c
            localmatrix[N - i][c] = mlist[i][j]
            j += 1
        # right column
        for r in xrange(N - i - 1, i, -1):
            if debug&2: print "right column:", r, M - i - 2
            localmatrix[r][M - i - 2] = mlist[i][j]
            j += 1
        # upper row
        for c in xrange(M - i - 2, i, -1):
            if debug&2: print "upper row:", i, c
            localmatrix[i][c] = mlist[i][j]
            j += 1
    return localmatrix


def rotatematrix(mlist, rotations):
    if debug & 4: print"\n***rotatematrix***"
    newlist = mlist
    return newlist


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
