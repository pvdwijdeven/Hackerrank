# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:33:09 2016

@author: Pascal van de Wijdeven
"""
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
vectorizer = TfidfVectorizer()

try:
    filename = "SampleInput.txt"
    f = open(filename)
except:
    f= sys.stdin

def getbest(hdict,teamline):
    teamline=teamline.replace(" ","")
    teamline=teamline.replace("\n","")
    teamline=teamline.split(",")
    team1=0
    team2=0
    for i in range(0,5):
        team1=team1+hdict[teamline[i]][2]
    for i in range(5,10):
        team2=team2+hdict[teamline[i]][2]
    return 1 if team1>team2 else 2
    


SampleInput=f.readlines()
for x in range(len(SampleInput)):
    SampleInput[x]=SampleInput[x].replace('\n',"")
f.close

filename = "trainingdata.txt"
f = open(filename)

Trainingdata=f.readlines()

Heroes={}

winlose_X=[]
winlose_Y=[]

for x in Trainingdata:
    cur_data=x.split(",")
    cur_win=int(cur_data.pop())
    thisteam=""
    for i in range(0,5):
        thisteam+=" "+(cur_data[i].replace(" ",""))
    winlose_Y.append(-1*(cur_win-2))
    winlose_X.append(thisteam.strip())
    thisteam=""
    for i in range(5,10):
        thisteam+=" "+(cur_data[i].replace(" ",""))
    winlose_Y.append(cur_win-1)
    winlose_X.append(thisteam.strip())

bag_of_words=vectorizer.fit(winlose_X)
bag_of_words=vectorizer.transform(winlose_X)

test_X_team1=[]
test_X_team2=[]
nsamp=int(SampleInput[0])
for i in range(1,nsamp+1):
    players=SampleInput[i].split(",")
    team1=""
    team2=""
    for j in range(10):
        if j<5:
            team1+=" "+players[j].replace(" ","")
        else:
            team2+=" "+players[j].replace(" ","")
    test_X_team1.append(team1)
    test_X_team2.append(team2)
clf=LinearSVC(C=0.95)
clf.fit(bag_of_words,winlose_Y)
test_X_team1=vectorizer.transform(test_X_team1)
test_X_team2=vectorizer.transform(test_X_team2)
test_Y_team1=clf.predict(test_X_team1)
test_Y_team2=clf.predict(test_X_team2)

for x in Trainingdata:
    cur_data=x
    cur_data=cur_data.replace("\n","")
    cur_data=cur_data.replace(" ","")
    cur_data=cur_data.split(",")
    cur_win=cur_data.pop()
    for y in range(len(cur_data)):
        winloose=(1-y//5) if int(cur_win)==1 else (y//5)
        if cur_data[y] in Heroes:
                Heroes[cur_data[y]][0]+=1
                Heroes[cur_data[y]][1]+=winloose
        else:
            Heroes[cur_data[y]]=[1,winloose]
for h in Heroes:
    Heroes[h].append(float(Heroes[h][1])/Heroes[h][0])

for i in range(len(test_Y_team1)):
    print getbest(Heroes,SampleInput[i+1])
