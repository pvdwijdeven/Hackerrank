# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:40:11 2016

@author: pvandewijdeven
"""

# Standard scientific Python imports

import math
import sys
from sklearn import datasets, svm

fontdict={
'00011000001111000110011011000011110000111100001111000011011001100011110000011000':'0',
'00011000001110000111100000011000000110000001100000011000000110000001100001111110':'1',
'00111100011001101100001100000011000001100000110000011000001100000110000011111111':'2',
'01111100110001100000001100000110000111000000011000000011000000111100011001111100':'3',
'00000110000011100001111000110110011001101100011011111111000001100000011000000110':'4',
'11111110110000001100000011011100111001100000001100000011110000110110011000111100':'5',
'00111100011001101100001011000000110111001110011011000011110000110110011000111100':'6',
'11111111000000110000001100000110000011000001100000110000011000001100000011000000':'7',
'00111100011001101100001101100110001111000110011011000011110000110110011000111100':'8',
'00111100011001101100001111000011011001110011101100000011010000110110011000111100':'9'
}

try:
    filename = "3.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

tresh=10
xscale=8
yscale=8

def getColorTresh(rgb,tresh):
    grey= 16-int((rgb[0] * 0.11 + rgb[1]* 0.59 + rgb[2]* 0.3)/16)
    return 0 if grey>tresh else 16

# The digits dataset
digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))


n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
classifier = svm.SVC(gamma=0.001)
classifier.fit(data, digits.target)


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
predIm=[]
for i in range(8):
    for j in range(8):
        predIm.append(newImage[j][i])



if sum(predIm)>64*8:
    for x in range(len(predIm)):
        predIm[x]=16-predIm[x]

predicted = classifier.predict([predIm]) 

print predicted[0]

if local:
    import matplotlib.pyplot as plt
    i=0
    j=0
    for x in predIm:
        
        digits.images[n_samples / 2][i][j]=x
        i+=1
        if i==8:
            i=0
            j+=1
    
    images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
    for index, (image, prediction) in enumerate(images_and_predictions[:4]):
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Prediction: %i' % predicted[0])
    plt.show()