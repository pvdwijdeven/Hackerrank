# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:56:18 2016

@author: pvandewijdeven
"""

neighbours=[]   # list of neighbours per house
debug = True
totList=[]
totValues=[]
roads=[]

def visitHouse(housesToVisit,level,curList):
    startList=list(curList)
    global totlist
    for house in housesToVisit:
        if debug: print "Visiting house: ", house, " level: ",level, " curList: ", 
        todo=list(housesToVisit)
        curList.append(house)
        if debug: print curList
        todo.remove(house)
        for neighbour in neighbours[house]:
            if neighbour in todo:
                todo.remove(neighbour)
        if todo<>[]:
            visitHouse(todo,level+1,curList)
            curList.pop()
        else:
            totList.append(list(curList))
            value=0
            for x in curList:
                value+=values[x]
            totValues.append(value)
            curList.pop()
    curList=list(startList)

if debug:
    N=4
    M=4
    values=[0,0,0,0]
    roads=[[1,2],[2,4],[4,3],[3,1]]
else:
    N,M=map(int,raw_input().split())
    values=map(int,raw_input().split())
    for _ in range(M):
        roads.append(map(int,raw_input().split()))

for house in xrange(N):
    neighbour=[]
    for road_ in roads:
        if road_[1]==house+1:
            neighbour.append(road_[0]-1)
        if road_[0]==house+1:
            neighbour.append(road_[1]-1)
    neighbours.append(neighbour)

visitHouse(range(N),0,[])
if debug: print "totList: ", totList
if debug: print "totValues: ", totValues

maxValue=max(totValues)

maxList=[]
for i in range(len(totValues)):
    if totValues[i]==maxValue:
        maxList.append(totList[i])
for i in range(len(maxList)):
    maxList[i].sort()
   
maxList = sorted(set(map(tuple, maxList)), reverse=True)
if debug: print "maxlist before 0 prizes: ", maxList

zeroList=[]
zeros=[]
for x in maxList:
    temp=[]
    count=0
    for y in x:
        if values[y]==0:
            count+=1
        else:
            temp.append(y)
    if count>0:
        zeroList.append(list(temp))
        zeros.append(count)

if debug: print "zeroList: ", zeroList
if debug: print "zeros: ", zeros
zerosValue=0
for x in zeros:
    zerosValue+=(2**x)-1

print maxValue,
print len(maxList)+zerosValue-(len(zeroList)-len(sorted(set(map(tuple, zeroList)), reverse=True)))