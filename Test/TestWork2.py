#!/usr/bin/py

donelist = []


def ask(nn):
    for x in xrange(0, vals[0]):
        nextitem = nn + 1
        if x != nn and x not in query[nn].keys():
            print nn, x
            return
        elif x != nn:
            # todo: none for all previous items
            if not query[nn][x]:
                nextitem = x
    donelist.append(x)
    if len(donelist) > vals[3] + 2:
        # just pick biggest YES
        answer()
    else:
        ask(nextitem)


def answer():
    maxfound = 0
    maxx = -1
    for x in donelist:
        found = 0
        for y in query[x].keys():
            if query[x][y] == 1:
                found += 1
        if maxfound <= found:
            maxx = y
            maxfound = found
    print maxx


def nextQuestion(n, plurality, lies, color, exact_lies, query):
    nfactor = (n - 2 * plurality) / (color * 2 - 1)
    if exact_lies > 0:
        liesf = lies / 4
    else:
        liesf = exact_lies / 2
    for x in xrange(0, n):
        no = 0
        yes = 0
        for y in query[x].keys():
            if query[x][y] == 0:
                no += 1
            else:
                yes += 1
        if yes >= liesf + nfactor and query_size >= (lies + 1) * n / 2:
            print x
            return
        elif no <= liesf + nfactor:
            ask(x)
            return
        else:
            donelist.append(x)
            if len(donelist) > vals[3] + 2:
                # just pick biggest YES
                answer()


if __name__ == '__main__':
    vals = [int(i) for i in raw_input().strip().split()]
    query_size = input()
    query = {}
    for i in range(vals[0]):
        query[i] = {}

    for i in range(query_size):
        temp = [j for j in raw_input().strip().split()]
        if temp[2] == "YES":
            query[int(temp[0])][int(temp[1])] = 1
            query[int(temp[1])][int(temp[0])] = 1
        else:
            query[int(temp[0])][int(temp[1])] = 0
            query[int(temp[1])][int(temp[0])] = 0

    nextQuestion(vals[0], vals[1], vals[2], vals[3], vals[4], query)
