# -*- coding: utf-8 -*-

"""
Hackerrank - Algorithms - Strings

Author: PvdWijdeven
"""
# !/usr/bin/py
import random


def create_overview():
    for x in xrange(vals[0]):
        no = 0
        yes = 0
        source = 0
        for y in query[x].keys():
            if query[x][y][0] == 0:
                no += 1
            else:
                yes += 1
            source = query[x][y][1]
        max_candidate = 1 if yes > minyes else 0
        done = 1 if yes + no > mintot or no > minno else 0
        # format: [#no, #yes, maxCandidate, Done, Source]
        overview.append([no, yes, max_candidate, done, source])

    return


def ask(qval):
    # Ask for new value
    while True:
        x = random.randint(0, n - 1)
        if x not in query[qval].keys():
            print qval, x
            return


def next_fill():
    # first find if action has to be finished
    for x in xrange(n):
        if overview[x][4] and overview[x][0] + overview[x][1] > 0:
            # already started with this ball
            if overview[x][3] != 1:
                # not done yet, continue asking
                ask(x)
                return
    # no current actions found, pick random one!
    while True:
        x = random.randint(0, n - 1)
        if overview[x][3] != 1:
            ask(x)
            return


def next_question():
    create_overview()
    if onemore:
        next_fill()
        return
    else:
        # check for candidates
        candidates = []
        for x in xrange(n):
            if overview[x][2] == 1:
                candidates.append([x, -1])
        if len(candidates) == 0:
            # no candidates found, keep searching
            next_fill
            return
        elif len(candidates) == 1:
            # 1 candidate found should be the one
            print candidates[0][0]
            return
        else:
            # multiple candidates found, try to find if in same group
            for i, can in enumerate(candidates):
                x = can[0]
                c = can[1]
                if c == -1:
                    # not in group yet
                    candidates[i] = [x, x]
                    for j, y in enumerate(candidates):
                        if query[x][y[0]][0] == 1:
                            candidates[j] == [y[0], x]
            grpdict = {}
            for x, c in candidates:
                # select ball from biggest group
                if c in grpdict:
                    grpdict[c] += 1
                else:
                    grpdict[c] = 1
            maxval = 0
            maxkey = -1
            doublemax = False
            for x in grpdict.keys():
                if grpdict[x] > maxval:
                    maxval = grpdict[x]
                    maxkey = x
                    doublemax = False
                elif grpdict[x] == maxval:
                    doublemax = True
            if doublemax:
                # ex-equo found, search further
                next_fill()
                return
            else:
                # max group found
                print maxkey
                return


if __name__ == '__main__':
    vals = [int(i) for i in raw_input().strip().split()]
    query_size = input()
    query = {}
    for i in range(vals[0]):
        query[i] = {}

    for i in range(query_size):
        temp = [j for j in raw_input().strip().split()]
        if temp[2] == "YES":
            query[int(temp[0])][int(temp[1])] = [1, 1]
            query[int(temp[1])][int(temp[0])] = [1, 0]
        else:
            query[int(temp[0])][int(temp[1])] = [0, 1]
            query[int(temp[1])][int(temp[0])] = [0, 0]
    onemore = query_size < (vals[2] + 1) * vals[0] / 2
    n = vals[0]
    plurality = vals[1]
    lies = vals[2]
    color = vals[3]
    exact_lies = vals[4]

    # todo: find optimal factor
    factor = 0.7
    minyes = n / color * 0.8
    minno = (color - 1) * n / color * 0.6
    mintot = n * factor
    overview = []

    next_question()
