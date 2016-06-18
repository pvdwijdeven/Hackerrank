# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 08:21:03 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn.linear_model import LogisticRegression

#make sure it works both local and online
try:
    filename = "SampleInput.txt"
    f = open(filename)
except:
    f= sys.stdin

test_X=[]
games=[]
test_games=[]
train_X=[]
train_Y=[]
list_heroes=[]
dict_heroes={}

#import test case
SampleInput=f.readlines()
for x in range(len(SampleInput)):
    if x==0:
        ntest=int(SampleInput[x])
    else:
        test_games.append((SampleInput[x].replace('\n',"")).split(","))
f.close

#Import training dataset
filename = "trainingdata.txt"
f = open(filename)
Trainingdata=f.readlines()
for x in range(len(Trainingdata)):
    games.append((Trainingdata[x].replace('\n',"")).split(","))

#create list/dict with heroes
for x in games:
    for y in x:
        list_heroes.append(y)
list_heroes=list(set(list_heroes))
for i in range(len(list_heroes)):
    dict_heroes[list_heroes[i]]=i

#create trainingset with all features 0 and set to 1 if heroe in team1 else -1
for i in range(len(games)):
    curteam=[0]*len(list_heroes)
    for j in range(0,5):
        curteam[dict_heroes[games[i][j]]]=-1
    for j in range(5,10):
        curteam[dict_heroes[games[i][j]]]=1
    train_X.append(curteam)
    Y=1 if int(games[i][10])==1 else -1
    train_Y.append(Y)

#train data
LR=LogisticRegression(C=0.055).fit(train_X,train_Y)

#create testset with all features 0 and set to 1 if heroe in team1 else -1
for i in range(len(test_games)):
    curteam=[0]*len(list_heroes)
    for j in range(0,5):
        curteam[dict_heroes[test_games[i][j]]]=-1
    for j in range(5,10):
        curteam[dict_heroes[test_games[i][j]]]=1
    test_X.append(curteam)
    
#### Predict the result    
test_Y = LR.predict(test_X)
for i in range(0,len(test_Y)):
    print 1 if test_Y[i]==1 else 2