# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:40:11 2016

@author: pvandewijdeven
"""
import sys
import math
from sklearn import datasets, svm

digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
classifier = svm.SVC(gamma=0.001)
classifier.fit(data, digits.target)


try:
    filename = "sampleinput.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

xscale=8
yscale=8

def getColorTresh(rgb,tresh):
    if (rgb[0] * 0.3 + rgb[1]* 0.59 + rgb[2]* 0.11)<tresh:
        return 0
    else:
        return 1
    

tresh=50
xcounter=0
newImage=[]
nrows,ncols=map(int,(f.readline().strip()).split(' '))
for y in range(nrows):
    line=(f.readline().strip()).split(" ")
    if y%math.ceil(nrows/float(yscale))==0:
        newImageLine=[]
        for x in range(ncols):
            if x%math.ceil(ncols/float(xscale))==0:
                rgb=map(int,line[x].split(","))
                newImageLine.append(getColorTresh(rgb,tresh))
        newImage.append(newImageLine)

zz=0
for x in newImage:
    zz=zz+sum(x)
if zz>xscale*yscale/2:
    for x in range(xscale):
        for y in range(yscale):
            newImage[y][x]=newImage[y][x]*-1 + 1

print newImage

        

predIm=[]
for x in newImage:
    for y in x:
        predIm.append(y)
        print y,
    print
        

predicted = classifier.predict([predIm]) 
print predicted[0]

