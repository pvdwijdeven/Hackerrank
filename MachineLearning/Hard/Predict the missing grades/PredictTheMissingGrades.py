# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 08:21:03 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn.linear_model import SGDRegressor
import json
import numpy

SubjDict= {'serial':0, 'English':1,'Physics':2,'Chemistry':3,
           'ComputerScience':4,'Biology':5,'PhysicalEducation':6,
           'Economics':7,'Accountancy':8,'BusinessStudies':9}

#make sure it works both local and online
try:
    filename = "sample-test2.in.json"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

#Initialize training/test data
train_X=[]
train_Y=[]
test_X=[]
test_Y=[]

#import test case
ntest=int(f.readline())
for i in range(ntest):
    jsondata=json.loads(f.readline())
    #if not part of cases
    data=[0]*(len(SubjDict)+1)
    for j in jsondata.keys():
        if j in SubjDict:
            data[SubjDict[j]]=jsondata[j]
    test_X.append(data)
f.close()

#import training data
filename = "training.json"
f = open(filename)
ntrain=int(f.readline())
for i in range(ntrain):
    jsondata=json.loads(f.readline())
    #if not part of cases
    data=[0]*(len(SubjDict)+1)
    for j in jsondata.keys():
        if j in SubjDict:
            data[SubjDict[j]]=jsondata[j]
    train_X.append(data)
    train_Y.append(jsondata['Mathematics'])
f.close()

#fit/train data
train_X=numpy.array(train_X)
test_X=numpy.array(test_X)
rsmax=0
zmax=0
LR=SGDRegressor(epsilon=0.17,fit_intercept=False,penalty='elasticnet',
                loss='epsilon_insensitive',random_state=692,alpha=0.000001,
                n_iter=4).fit(train_X[:,1:],train_Y)
test_Y = LR.predict(test_X[:,1:])
for i in range(len(test_Y)):
    if test_Y[i]<2:
        test_Y[i]=2
    elif test_Y[i]>7:
        test_Y[i]=7


#### Predict the result    
if local:
    #import test output
    filename = "sample-test2.out.json"
    f = open(filename)
    z=0
    for x in test_Y:
        y=int(f.readline())
        if int(x)<=int(y)+1 and int(x)>=int(y)-1:
            z=z+1
    print 100*(z-(len(test_Y)-z))/float(len(test_Y))
else:
    for x in test_Y:
        print int(x)
