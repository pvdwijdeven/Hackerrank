# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:05:23 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

testCase=4      #select test case 1,2,3, for offline use only
fitbefore=1     #number of items to fit before
fitafter=1      #number of items to fit after
polydegree=2    #poly-degree for fit

#make sure both online and offline will work
try:
    filename = "SampleInput"+str(testCase)+".txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

Train_total=[]
Test_total=[]
Train_X=[]
Train_Y=[]
Test_X=[]
Test_Y=[]
TrainDict={}

#read input
n=int(f.readline())
for i in range(n):
    data=f.readline().split("\t") 
    if data[1][0]=="M":
        Test_total.append([data[0],i,data[1]])
        Test_X.append([i])
    else:
        Train_total.append([data[0],i,float(data[1])])
        TrainDict[i]=len(Train_total)-1
#        Train_X.append([i])
#        Train_Y.append(float(data[1]))


poly = PolynomialFeatures(degree=polydegree)
clf = linear_model.LinearRegression()

#print TrainDict

for x in range(20):
    Train_X=[]
    Train_Y=[]
    position=int(Test_X[x][0])
#    print position
    for i in range(fitbefore,0,-1):
        curpos=position-i
#        print curpos
        if curpos in TrainDict:
#            print TrainDict[curpos]
#            print Train_total[TrainDict[curpos]]
            Train_X.append([Train_total[TrainDict[curpos]][1]])
            Train_Y.append([Train_total[TrainDict[curpos]][2]])
    for i in range(fitafter):
        curpos=position+i+1
        if curpos in TrainDict:
            Train_X.append([Train_total[TrainDict[curpos]][1]])
            Train_Y.append([Train_total[TrainDict[curpos]][2]])
#        print curpos
#    print Train_X
#    print
    
    if Train_X<>[]:
        Train_XP = poly.fit_transform(Train_X)
        
    
        clf.fit(Train_XP, Train_Y)
        Test_XP=poly.fit_transform(Test_X[x])
    #    print Test_XP
    #    print clf.predict([Test_XP[0]])[0][0]
        Test_Y.append(clf.predict(Test_XP[0])[0])
        
    else:
        Test_Y.append(Test_Y[x-1])
#print Test_Y

if not local:
    for x in Test_Y:
        print format(float(x[0]) ,'.2f')
else:
    filename = "SampleOutput"+str(testCase)+".txt"
    f = open(filename)
    totald=0
    for x in Test_Y:
        pred=float(format(x[0],'.2f'))        
        actual=float(f.readline())
        d=abs((actual-pred)/actual)*100
        print str(actual)+"\t"+str(pred)+"\t"+str(d)
        totald+=d
    print 50*max(2-totald,0)