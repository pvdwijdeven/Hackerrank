# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:00:29 2016

@author: pvandewijdeven
"""
from PIL import Image
import os

def getColorGrey(rgb):
    x= (16-int((rgb[0] * 0.11 + rgb[1]* 0.59 + rgb[2]* 0.3)/16))/16.0
    return int(x*10)

def getColor(image,y,x,ratiox,ratioy):
    xtot=0.0
    for i in range(y-int(ratioy*0.5),y+int(ratiox*0.5)):
        xtot+=sum(image[i][x-int(ratiox*.5):x+int(ratiox*.5)])
    return round(xtot/(ratiox*ratioy),1)


trainingdata=[]
for fld in range(10):

    for fn in os.listdir(os.getcwd()+'/digits/'+str(fld)+'/'):
        lim=3
        counter=0
        if fn.endswith(".png"):
            counter+=1
            if counter>lim: break
            filename = "digits/"+str(fld)+"/"+fn
            im=Image.open(filename)
            curImage=im.load()
            ncols,nrows =  im.size
            print curImage[25,25]
            
            xscale=ncols#15
            yscale=nrows#20
            
            
            ratiox=ncols/float(xscale+1)
            ratioy=nrows/float(yscale+1)
            
            newImage=[]
            for y in range(0,yscale):
                newLine=[]
                for x in range(0,xscale):
                    newLine.append((curImage[x,y]))
                newImage.append(newLine)
            
            total=0
            for x in newImage:
                for y in x:
                    total+=y
            if total/float(xscale*yscale)>10000:
                for i in range(yscale):
                    for j in range(xscale):
                        newImage[i][j]=10-newImage[i][j]
            predIm=[]
            for i in range(xscale):
                for j in range(yscale):
                    predIm.append(newImage[j][i])
            
#            print predIm
            trainingdata.append(predIm)
        else:
            continue
print trainingdata