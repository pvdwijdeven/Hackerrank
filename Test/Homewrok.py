#!/usr/bin/py
# todo: check every value until >lies NO or YES
# todo: if NO --> next until YES and queries >=(lies+1) *n/2

factor=3

def ask(nn):
    for x in xrange(0,vals[0]):
        if x!=nn and not x in query[nn].keys():
            print nn,x
            return
    ask(nn+1)

def nextQuestion(n, plurality, lies, color, exact_lies, query):
    result=-1
    for x in xrange(0,n):
        no=0
        yes=0
        for y in query[x].keys():
            if query[x][y]==0:
                no+=1
            else:
                yes+=1
        if yes>=lies+(n/factor) and query_size>=(lies+1)*n/2:
            print x
            return
        elif no <= lies + (n / factor):
            ask(x)
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
            query[int(temp[0])][int(temp[1])] = 1
            query[int(temp[1])][int(temp[0])] = 1
        else:
            query[int(temp[0])][int(temp[1])] = 0
            query[int(temp[1])][int(temp[0])] = 0

    nextQuestion(vals[0], vals[1], vals[2], vals[3], vals[4], query)
