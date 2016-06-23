# -*- coding: utf-8 -*-
"""
Captcha Cracker - create fonts

Pascal van de Wijdeven
"""
threshold=300
fontdict={}
#font = 8x10
#space between fonts=1
#1st letter starts at: [11,5]
#2nd letter starts at: [11,15]
#3rd letter starts at: [11,25]
#4th letter starts at: [11,35]
#5th letter starts at: [11,45]



for j in range(25):
    xx= "{0:0>2}".format(j)
    filename="input\input"+xx+".txt"
    f=open(filename)
    nrows,ncols=map(int,f.readline().split(" " ))
    
    newpict=[]
    for r in range(nrows):
        row=f.readline().split(" ")
        newrow=[]
        for c in row:
            r,g,b=map(int,c.split(","))
            newrow.append(1 if r+g+b<threshold else 0)
        newpict.append(newrow)
    f.close
    
    
    filename="output\output"+xx+".txt"
    f=open(filename)
    captcha=f.readline().strip()
    startx=5
    starty=11
    for i in range(len(captcha)):
        chaptchar=captcha[i]
        capfont=""
        for y in range(10):
            for x in range(8):
                capfont+="0" if newpict[starty+y][startx+x]==0 else "1"
        startx+=9
        fontdict[chaptchar]=capfont
klist=fontdict.keys()
for x in sorted(klist):
    print "'" + fontdict[x] + "':'"+ x +"',"

