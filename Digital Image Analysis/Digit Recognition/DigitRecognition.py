# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:40:11 2016

@author: pvandewijdeven
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt
import numpy as np
import math
# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 3 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# pylab.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])

# Now predict the value of the digit on the second half:
expected = digits.target[n_samples / 2:]
predicted = classifier.predict(data[n_samples / 2:])
i=0
j=0
for x in [15, 15, 15, 15, 15, 15, 15, 15, 15, 9, 1, 1, 0, 0, 0, 7, 15, 1, 1, 1, 0, 0, 0, 0, 15, 1, 13, 13, 0, 0, 11, 0, 15, 1, 13, 1, 0, 0, 11, 0, 15, 1, 13, 1, 0, 11, 11, 0, 15, 1, 1, 1, 0, 0, 0, 0, 15, 1, 1, 1, 0, 0, 0, 0]:
    
    digits.images[n_samples / 2][i][j]=x
    i+=1
    if i==8:
        i=0
        j+=1
        
i=0
j=0
for x in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 2, 16, 16, 16, 16, 16, 16, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
    
    digits.images[n_samples / 2+1][i][j]=x
    i+=1
    if i==8:
        i=0
        j+=1


i=0
j=0
for x in [0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 7, 7, 7]:
    
    digits.images[n_samples / 2+2][i][j]=x
    i+=1
    if i==8:
        i=0
        j+=1
 



try:
    filename = "SampleText1.txt"
    f = open(filename)
    local=True
except:
    f= sys.stdin
    local=False

xscale=8
yscale=8

def getColorTresh(rgb,tresh):
    return 16-int((rgb[0] * 0.11 + rgb[1]* 0.59 + rgb[2]* 0.3)/16)

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
predIm=[]
for i in range(8):
    for j in range(8):
        predIm.append(newImage[j][i])

if sum(predIm)>64*8:
    for x in range(len(predIm)):
        predIm[x]=16-predIm[x]

#print predIm
predicted = classifier.predict([predIm]) 
#print predicted[0]

i=0
j=0
for x in predIm:
    
    digits.images[n_samples / 2+3][i][j]=x
    i+=1
    if i==8:
        i=0
        j+=1
x=[1,2,3,4]

images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
#print images_and_predictions[0]
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)
#print images_and_labels[0]
plt.show()