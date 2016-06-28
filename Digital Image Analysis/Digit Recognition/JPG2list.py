# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:02:30 2016

@author: pvandewijdeven
"""

import PIL
import numpy as np
image = np.asarray(PIL.Image.open('img02_1.jpg'))
f=open('1.txt','w')
f.write(str(len(image))+","+str(len(image[0]))+"\n")
for x in image:
    for y in x:
        f.write(str(y[0])+"," +str(y[1])+","+str(y[2])+" ")
    f.write("\n")
f.close()