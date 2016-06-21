# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:24:39 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import datetime
Train_X=[]
Train_Y=[]
dates=[]
#make sure it works both local and online
try:
    filename = "SampleInput2.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False
date_list=[]


ntest=int(f.readline())
#import data 
for i in range(ntest):
    traffic=int(f.readline())
    Train_Y.append(traffic)

oneday=datetime.timedelta(days=1)
dt = datetime.datetime(2012, 10, 01)
for i in range(ntest+30):
    dates.append(dt+(i*oneday))

for x in dates:
    Train_X.append([x.year,x.month,x.day,1 if x.weekday()==0 else 0,
                    1 if x.weekday()==1 else 0,1 if x.weekday()==2 else 0,
                    1 if x.weekday()==3 else 0,1 if x.weekday()==4 else 0,
                    1 if x.weekday()==5 else 0,1 if x.weekday()==6 else 0,
                    x.isocalendar()[1]])


poly = PolynomialFeatures(degree=1)
Train_X=poly.fit_transform(Train_X)

Test_X=Train_X[-30:]
Train_X=Train_X[:-30]

LR = LinearRegression(normalize=True,fit_intercept=False).fit(Train_X,Train_Y)
Test_Y=LR.predict(Test_X)-237


if local:
    filename = "SampleOutput2.txt"
    f = open(filename)
    dtot=0.0
    k=0
    for x in Test_Y:
        actual=int(f.readline())
        d=(abs(actual-int(x))/float(actual))/30
        print int(x),actual,d
        dtot+=d
    print 5*max(20-(dtot*100),0)
else:
    for x in Test_Y:
        print int(x)
