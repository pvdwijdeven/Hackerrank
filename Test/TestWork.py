# -*- coding: utf-8 -*-
"""
Pascal van de Wijdeven
"""

roads=[]
neighbours=[]
maxList=[]
curList=[[]]
maxAmount=0
maxValue=0
test=True
counter=0
curValue=[0]

if test:
    N=6
    M=5
    values=[1,2,4,8,16,32]
    roads=[[1,2],[2,3],[3,4],[4,5],[5,6]]
else:
    N,M=map(int,raw_input().split())
    values=map(int,raw_input().split())
    for _ in range(M):
        roads.append(map(int,raw_input().split()))

def addHouse(todo, doneSoFar, valueSoFar):
    if test: print "addHouse entered"
    global curList
    global curValue
    global counter
    mytodo=[]
    for x in todo:
        mytodo.append(x)
    for house in mytodo:
        curValue[counter]+=values[house]
        if todo==range(N): 
            if test: print "=======NEWHOUSE========", house
            doneSoFar=[]
            valueSoFar=0
        else:
            if test: print "house:", house
        todo.remove(house)
        doneSoFar.append(house)
        valueSoFar+=values[house]
        print "doneSoFar:", doneSoFar, "value so far:",valueSoFar
        for neighbour in neighbours[house]:
            if neighbour in todo:
                todo.remove(neighbour)
        if test:
            print "todo:", todo
            print "doneSoFar:", doneSoFar
        if todo==[]:
            counter+=1
            curValue.append(0)
            valueSoFar-=doneSoFar.pop()
            curList.append(list(doneSoFar))
            todo=[]
            for x in mytodo:
                todo.append(x)
        else:
            if test: print "new addhouse with todo:", todo
            addHouse(todo,doneSoFar,valueSoFar)
            if test: print "I'm back with todo:", todo, " and mytodo:", mytodo
            valueSoFar-=doneSoFar.pop()
            todo=[]
            for x in mytodo:
                todo.append(x)
        if test: print "curlist", curList[counter-1]
        if test: print "curValue", curValue[counter-1]

#create neighbour list, shift -1, so that it matches listindex
for house in range(N):
    neighbour=[]
    for road_ in roads:
        if road_[1]==house+1:
            neighbour.append(road_[0]-1)
        if road_[0]==house+1:
            neighbour.append(road_[1]-1)
    neighbours.append(neighbour)

if test: print "Neighbourlist:", neighbours

addHouse(range(N),[],0)
    
if test: print "curValue:", curValue
if test: print "curList:", curList
if test: print "counter:", counter

for i in range(len(curList)):
    curList[i].sort()

if test: print "curlist sorted:", curList

maxValue=max(curValue)


for i in range(len(curValue)):
    if curValue[i]==maxValue and curList[i]<>[]:
        maxList.append(curList[i])

if test: print "maxList:", maxList





zeroList=[]
zeroAmount=[]
for i in range(len(maxList)):
    zeros=0
    temp=[]
    for x in maxList[i]:
        if values[x]==0:
            zeros+=1
        else:
            temp.append(x)
    if zeros>0: 
        zeroList.append(temp)
        zeroAmount.append(zeros)

zeroList=map(tuple,zeroList)
if test: print "zerolist:", zeroList
zeroDict={}
for x in range(len(zeroList)):
    if zeroList[x] in zeroDict:
        if zeroDict[zeroList[x]]<zeroAmount[x]:
            zeroDict[zeroList[x]]=zeroAmount[x]
    else:
        zeroDict[zeroList[x]]=zeroAmount[x]

if test: print "zeroDict:", zeroDict
if test: print "zeroAmount:", zeroAmount

extra=0
for x in zeroDict:
    extra+=(2**zeroDict[x])-1
    
result = sorted(set(map(tuple, maxList)), reverse=True)
if test: print "unique result:", result
print maxValue,
print len(result)+extra