# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:24:39 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import  AdaBoostRegressor
Train_X=[]
Train_Y=[]
dates=[]
#make sure it works both local and online
try:
    filename = "SampleInput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False
date_list=[]


ntest=int(f.readline())
#import data 
for i in range(ntest):
    traffic=int((f.readline().split())[1])
    Train_Y.append(traffic)

for i in range(ntest+12):
    month=i%12
    Train_X.append([month,i//12,1 if month==0 else 0,
                   1 if month==1 else 0,1 if month==2 else 0,
                   1 if month==3 else 0,1 if month==4 else 0,
                   1 if month==5 else 0,1 if month==6 else 0,
                   1 if month==7 else 0,1 if month==8 else 0,
                   1 if month==9 else 0,1 if month==10 else 0,
                   1 if month==11 else 0,1 if month==12 else 0])




Test_X=Train_X[-12:]
Train_X=Train_X[:-12]
clf = AdaBoostRegressor(DecisionTreeRegressor(max_depth = 3), n_estimators = 37, learning_rate = 2).fit(Train_X,Train_Y)
Test_Y=clf.predict(Test_X)-90000


if local:
    filename = "SampleOutput.txt"
    f = open(filename)
    dtot=0.0
    k=0
    for x in Test_Y:
        actual=int(f.readline())
        d=(abs(actual-int(x))/float(actual))/12
        print int(x),actual,d
        dtot+=d
    print 2.5*max(40-(dtot*100),0)
else:
    for x in Test_Y:
        print int(x)
