# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:05:23 2016

@author: Pascal van de Wijdeven
"""
import sys
from sklearn.ensemble import GradientBoostingRegressor

DictMonths = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,
         "November":11,"December":12}


#Create Regressor
clf_min = GradientBoostingRegressor(n_estimators=128,learning_rate=115/1000.0,max_features=None)
clf_max = GradientBoostingRegressor(n_estimators=71,learning_rate=125/1000.0,max_features=None)
#make sure both online and offline will work
try:
    filename = "SampleInput2.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

#Initialize data
Train_total=[]
Test_total=[]
Train_X_Min=[]
Train_X_Max=[]
Train_Y_Min=[]
Train_Y_Max=[]
Test_X_Min=[]
Test_X_Max=[]
Test_Y_Min=[]
Test_Y_Max=[]
Test_Y=[]

startyear=-999
#read input
n=int(f.readline())
skip=f.readline()
for i in range(n):
    data=f.readline().split("\t")
    curmonth=DictMonths[data[1]]
    #missing data?
    if data[2][0]=="M" or data[3][0]=="M":
        Test_total.append([int(data[0]),data[1],data[2],data[3],curmonth])
    else:
        Train_total.append([int(data[0]),data[1],float(data[2]),float(data[3]),curmonth])



#create 2 testsets, one for missing MAX and one for missing MIN
for x in Test_total:
    if x[2][0]=="M":
        Test_X_Min.append([x[0],x[4],float(x[3])])
    else:
        Test_X_Max.append([x[0],x[4],float(x[2])])
        
#create 2 training and testsets: one for missing MAX and one for missing MIN:
for x in Train_total:
    Train_X_Min.append([x[0],x[4],x[3]])
    Train_Y_Min.append(x[2])
    Train_X_Max.append([x[0],x[4],x[2]])
    Train_Y_Max.append(x[3])


#train and predict, per case
clf_max.fit(Train_X_Max, Train_Y_Max)
Test_Y_Max=clf_max.predict(Test_X_Max)
clf_min.fit(Train_X_Min, Train_Y_Min)
Test_Y_Min=clf_min.predict(Test_X_Min)

#convert from numpy array back to list
Test_Y_Min=Test_Y_Min.tolist()
Test_Y_Max=Test_Y_Max.tolist()

#Merge min + max results together in 1 list
for x in Test_total:
    if x[2][0]=="M":
        Test_Y.append(Test_Y_Min[0])
        Test_Y_Min.remove(Test_Y_Min[0])
    else:
        Test_Y.append(Test_Y_Max[0])
        Test_Y_Max.remove(Test_Y_Max[0])

#Print results
if not local:
    for x in Test_Y:
        print format(float(x) ,'.1f')
else:
    filename = "SampleOutput2.txt"
    f = open(filename)
    totald=0
    for x in Test_Y:
        pred=float(format(x,'.1f'))        
        actual=float(f.readline())
        d=abs(actual-pred)
        print str(actual)+"\t"+str(pred)+"\t"+str(d)
        totald+=d
    score=(1-((float(totald)/len(Test_Y))/5.0))*100
    print "score:" + str(format(score,'.2f'))
