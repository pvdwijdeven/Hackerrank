# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 07:23:21 2016

@author: pvandewijdeven

"""

import math

debug=True
points=[]
N=0
angleList=[]

def getInput():
    global N
    global points
    if debug:
        N=5
        points=[[0,0],[0,1],[2,0],[1,1]]
    else:
        N=input()
        points=[]
        for _ in range(N):
            points.append(map(int,raw_input().split()))

def calculateAngle(a,b):
    if a[1]==b[1]:
        result=90 if a[0]<b[0] else -90
    elif a[0]==b[0]:
        result=0 if a[1]<b[1] else 180

    else:
        result=math.atan((a[0]-b[0])/(a[1]-b[1]))/(2*math.pi/360)
        #if result<0: result+=180
    return result

def createAngleList():
    if debug: print "starting creating angle list:"
    for a in points:
        pointList=[]
        for b in points:
            if a<>b:
                angle=calculateAngle(a,b)
                pointList.append(angle)
                pointList.sort()
        angleList.append(pointList)

def printAngleList():
    counter=0
    for x in angleList:
        print points[counter],":",x
        counter+=1

def getAmountofPoints(start,end,point):
    z=angleList[point]
    result=0
    if end>180: end=-(360-end)
    if start>180: start=-(360-start)
    if end<-180: end=360+end
    if start<-180: end=360+start
    if debug: print "start:",start," end:",end
    # start<end and start-end=90
    if start>90:
        for x in reversed(z):
            if x>=start:
                result+=1
            else:
                break
        start=-180
    for x in z:
        if x<end:
            if x>=start:
                result+=1
        else:
            break

    return result



def countsNs():
    totalN=0
    for i in xrange(len(points)):
        b=points[i]
        for j in xrange(len(points)):
            if i<>j:
                c=points[j]
                angleBC=calculateAngle(b,c)
                aa=getAmountofPoints(angleBC-90, angleBC, i)
                dd=getAmountofPoints(angleBC+90, angleBC+180, j)

                if debug: print "b,c:",b,c,
                if debug: print "AA:", aa, "between:", angleBC-90, angleBC ,
                if debug: print "DD:",dd, "between:", angleBC+90, angleBC+180,
                if debug: print "angle:",angleBC,
                if debug: print "Ns found:", aa*dd
                if debug: print
                totalN+=aa*dd
    return totalN

print calculateAngle([1,1],[0,0])
print calculateAngle([1,1],[2,0])
print calculateAngle([1,1],[2,2])
print calculateAngle([1,1],[0,2])
getInput()
createAngleList()
if debug: printAngleList()
if debug: print "\ncounting:"
result=countsNs()
if debug: print "\nresult:",
print result