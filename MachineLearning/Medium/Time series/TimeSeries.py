# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:24:39 2016

@author: Pascal van de Wijdeven
"""

import sys
from sklearn import linear_model

#make sure it works both local and online
try:
    filename = "SampleInput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

Train_X=[]
Train_Y=[]
Test_X=[]

ntest=int(f.readline())
for i in range(ntest):
    data=int(f.readline())
    Train_X.append([i])
    Train_Y.append(data)

for i in range(ntest,ntest+30):
    Test_X.append([i])

clf = linear_model.LinearRegression().fit(Train_X,Train_Y)
Test_Y=clf.predict(Test_X)

for x in Test_Y:
    print x