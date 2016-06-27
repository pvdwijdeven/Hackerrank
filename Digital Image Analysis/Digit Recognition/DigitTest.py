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
 
i=0
j=0
for x in [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 5, 0, 2, 12, 10, 0, 0, 4, 11, 0, 0, 0, 3, 0, 0, 6, 2, 0, 8, 0, 5, 0, 0, 5, 0, 0, 8, 0, 4, 0, 0, 0, 1, 8, 4, 9, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    
    digits.images[n_samples / 2+3][i][j]=x
    i+=1
    if i==8:
        i=0
        j+=1
x=[1,2,3,4]

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
#digits.images[n_samples / 2]=np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 15, 15, 15, 15, 15, 15, 1, 15, 15, 3, 3, 3, 15, 15, 1, 15, 15, 3, 15, 15, 15, 15, 1, 16, 16, 16, 16, 16, 16, 16, 1, 16, 16, 16, 16, 5, 16, 16, 1, 16, 16, 5, 5, 5, 16, 16, 1, 9, 16, 16, 16, 16, 16, 16])
images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
print images_and_predictions[0]
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)
print images_and_labels[0]
plt.show()
